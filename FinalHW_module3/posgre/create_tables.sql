CREATE TABLE IF NOT EXISTS user_sessions (
    session_id UUID PRIMARY KEY,
    user_id UUID,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    pages_visited JSONB,
    device JSONB,
    actions JSONB
);

CREATE TABLE IF NOT EXISTS product_price_history (
    product_id UUID PRIMARY KEY,
    price_changes JSONB,
    current_price INTEGER,
    currency VARCHAR(3)
);

CREATE TABLE IF NOT EXISTS event_logs (
    event_id UUID PRIMARY KEY,
    timestamp TIMESTAMP,
    event_type VARCHAR(50),
    details TEXT
);

CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id UUID PRIMARY KEY,
    user_id UUID,
    status VARCHAR(20),
    issue_type VARCHAR(50),
    messages TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_recommendations (
    user_id UUID PRIMARY KEY,
    recommended_products JSONB,
    last_updated TIMESTAMP
);

CREATE TABLE IF NOT EXISTS moderation_queue (
    review_id UUID PRIMARY KEY,
    user_id UUID,
    product_id UUID,
    review_text TEXT,
    rating INTEGER,
    moderation_status VARCHAR(20),
    flags JSONB,
    submitted_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS search_queries (
    query_id UUID PRIMARY KEY,
    user_id UUID,
    query_text TEXT,
    timestamp TIMESTAMP,
    filters JSONB,
    results_count INTEGER
);