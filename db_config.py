"""
Database Configuration for SQLite and PostgreSQL Support
Automatically detects PostgreSQL on Render, falls back to SQLite for local development
"""

import os
import sqlite3

# Check if PostgreSQL is available (Render provides DATABASE_URL)
DATABASE_URL = os.getenv('DATABASE_URL')
USE_POSTGRESQL = DATABASE_URL is not None

if USE_POSTGRESQL:
    # Fix Render's postgres:// to postgresql://
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    try:
        import psycopg2
        import psycopg2.extras
        print("✓ Using PostgreSQL database (Production Mode)")
    except ImportError:
        print("⚠️ psycopg2 not installed, falling back to SQLite")
        USE_POSTGRESQL = False
        DATABASE_URL = None

def get_db_connection():
    """Get database connection - PostgreSQL or SQLite"""
    if USE_POSTGRESQL:
        import psycopg2
        import psycopg2.extras
        conn = psycopg2.connect(DATABASE_URL)
        conn.row_factory = psycopg2.extras.RealDictCursor
        return conn
    else:
        # SQLite for local development
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn

def execute_query(query, params=None):
    """Execute a query and return results"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    
    try:
        results = cursor.fetchall()
    except:
        results = None
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return results

def init_db():
    """Initialize database schema for PostgreSQL or SQLite"""
    if USE_POSTGRESQL:
        init_postgresql()
    else:
        init_sqlite()

def init_postgresql():
    """Initialize PostgreSQL database"""
    import psycopg2
    
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Read and execute schema with PostgreSQL-compatible syntax
    with open('database.sql', 'r', encoding='utf-8') as f:
        schema = f.read()
        
        # Convert SQLite syntax to PostgreSQL
        schema = schema.replace('INTEGER PRIMARY KEY AUTOINCREMENT', 'SERIAL PRIMARY KEY')
        schema = schema.replace('TIMESTAMP DEFAULT CURRENT_TIMESTAMP', 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
        schema = schema.replace('INTEGER DEFAULT', 'INTEGER DEFAULT')
        schema = schema.replace('REAL DEFAULT', 'REAL DEFAULT')
        
        try:
            cursor.execute(schema)
            conn.commit()
            print("✓ PostgreSQL database initialized successfully")
        except psycopg2.errors.DuplicateTable:
            conn.rollback()
            print("✓ PostgreSQL database already initialized")
        except Exception as e:
            conn.rollback()
            print(f"Note: {e}")
    
    cursor.close()
    conn.close()

def init_sqlite():
    """Initialize SQLite database"""
    import sqlite3
    import os
    
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        with open('database.sql', 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("✓ SQLite database initialized successfully")
    else:
        # Run migrations for existing database
        conn = sqlite3.connect('database.db')
        try:
            # Check for service_catalog table
            result = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='service_catalog'"
            ).fetchone()
            
            if not result:
                print("🔄 Migrating SQLite database...")
                conn.executescript("""
                    CREATE TABLE IF NOT EXISTS service_catalog (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        service_name TEXT NOT NULL UNIQUE,
                        default_charge REAL DEFAULT 0,
                        is_active INTEGER DEFAULT 1,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    
                    CREATE INDEX IF NOT EXISTS idx_service_catalog_active ON service_catalog(is_active);
                """)
                conn.commit()
                print("✓ Service catalog added")
            
            # Add customer_date column if missing
            cursor = conn.execute("PRAGMA table_info(customers)")
            columns = [col[1] for col in cursor.fetchall()]
            if 'customer_date' not in columns:
                print("🔄 Adding customer_date column...")
                conn.execute("ALTER TABLE customers ADD COLUMN customer_date DATE")
                conn.commit()
                print("✓ Customer date field added")
            
            # Add search indexes
            conn.execute("CREATE INDEX IF NOT EXISTS idx_customers_name ON customers(name)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_customers_mobile ON customers(mobile)")
            conn.commit()
            print("✓ Customer search indexes added")
            
        except Exception as e:
            print(f"⚠️ Migration note: {e}")
        finally:
            conn.close()
