
CREATE INDEX idx_sales_created_at ON sales(created_at);
CREATE INDEX idx_sales_store_id ON sales(store_id);
CREATE INDEX idx_sales_sub_brand_id ON sales(sub_brand_id);
CREATE INDEX idx_sales_customer_id ON sales(customer_id);
CREATE INDEX idx_sales_channel_id ON sales(channel_id);
CREATE INDEX idx_sales_status_desc ON sales(sale_status_desc);

CREATE INDEX idx_payments_sale_id ON payments(sale_id);
CREATE INDEX idx_payments_payment_type_id ON payments(payment_type_id);

CREATE INDEX idx_stores_brand_id ON stores(brand_id);
CREATE INDEX idx_stores_sub_brand_id ON stores(sub_brand_id);
CREATE INDEX idx_stores_state ON stores(state);
CREATE INDEX idx_stores_city ON stores(city);

CREATE INDEX idx_customers_store_id ON customers(store_id);
CREATE INDEX idx_customers_sub_brand_id ON customers(sub_brand_id);
CREATE INDEX idx_customers_created_at ON customers(created_at);

CREATE INDEX idx_product_sales_sale_id ON product_sales(sale_id);
CREATE INDEX idx_product_sales_product_id ON product_sales(product_id);

CREATE INDEX idx_categories_brand_id ON categories(brand_id);
CREATE INDEX idx_channels_brand_id ON channels(brand_id);
CREATE INDEX idx_coupon_sales_sale_id ON coupon_sales(sale_id);
CREATE INDEX idx_coupon_sales_coupon_id ON coupon_sales(coupon_id);