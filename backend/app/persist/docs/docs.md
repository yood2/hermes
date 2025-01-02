# Database Schema

## January 1, 2025 - Draft 2

Made an associative table (Holdings) to connect users to their portfolios and
portfolios to their stocks. Also, changed variable names to match the SQLModel
naming conventions (camelCase).

### User Table

-   userId: string
-   name: string
-   createdAt: timestamp

### Portfolio Table

-   portfolioId: string
-   userId: string
-   createdAt: timestamp
-   updatedAt: timestamp

### Holdings Table

-   holdingId: string
-   portfolioId: string
-   stockId: string
-   quantity: int
-   purchasePrice: float
-   purchaseDate: timestamp
-   updatedAt: timestamp

### Stock Table

-   stockId: string
-   ticker: string
-   fullName: string
-   exchange: string
-   sector: string
-   createdAt: timestamp
-   updatedAt: timestamp

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
