# ZEKA REST microservice

## Quick start (local, dev)
1. Create `.env` with:

   MONGODB_URI="mongodb+srv://<user>:<pass>@zeka.7ijqrc1.mongodb.net/?retryWrites=true&w=majority"
   MONGODB_DB="ZEKA"

2. Create venv & install:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Run:
   python run.py

4. Endpoints:
   POST /api/customers  {name, email}
   GET  /api/customers
   POST /api/orders     {customer_id, item, amount}
