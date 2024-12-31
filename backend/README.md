# API Backend

#### Running the API

```bash
fastapi dev main.py
```

#### Installing Dependencies

```bash
pip install -r requirements.txt
```

#### When adding libraries:

1. `pip show <library>` to check library version
2. `echo "<library>==<version>" >> requirements.txt` to add the library to the
   requirements.txt file

#### Running Tests

```bash
python -m unittest tests/tests.py
```

# Database Schema

## December 30, 2024 - Draft 1

### User Table

-   user_id: string
-   created_at: timestamp

### Portfolio Table

-   portfolio_id: string
-   user_id: string
-   created_at: timestamp
-   updated_at: timestamp

### Holdings Table

-   holding_id: string
-   portfolio_id: string
-   ticker: string
-   quantity: int
-   price: float
-   created_at: timestamp
-   updated_at: timestamp

![Schema](./schema_dec30.png)
