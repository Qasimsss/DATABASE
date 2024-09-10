
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#postgres local
#DATABASE_URL = "postgresql://postgres:admin123@localhost/TestDB"

#supabase online
DATABASE_URL = "postgresql://postgres.ngwktlcudbvkszpkmtco:OYedRfPDIvS56YnF@aws-0-us-east-1.pooler.supabase.com:6543/postgres"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
