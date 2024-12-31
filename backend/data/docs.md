# Schema

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
