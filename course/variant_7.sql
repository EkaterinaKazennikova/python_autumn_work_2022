CREATE TABLE "filter" (
  "id" SERIAL PRIMARY KEY,
  "country" VARCHAR(100) NOT NULL,
  "city" VARCHAR(100) NOT NULL,
  "duration" INTEGER,
  "nutrition" VARCHAR(50) NOT NULL,
  "hotel" VARCHAR(50) NOT NULL,
  "included" VARCHAR(100) NOT NULL,
  "price" INTEGER
);

CREATE TABLE "workers" (
  "id" SERIAL PRIMARY KEY,
  "surname" VARCHAR(50) NOT NULL
);

CREATE TABLE "customers" (
  "id" SERIAL PRIMARY KEY,
  "workers" INTEGER NOT NULL,
  "surname" VARCHAR(50) NOT NULL,
  "age" DATE,
  "phone" INTEGER,
  "discount" BOOLEAN
);

CREATE INDEX "idx_customers__workers" ON "customers" ("workers");

ALTER TABLE "customers" ADD CONSTRAINT "fk_customers__workers" FOREIGN KEY ("workers") REFERENCES "workers" ("id") ON DELETE CASCADE;

CREATE TABLE "customers_filter" (
  "id_customers" INTEGER NOT NULL,
  "id_filter" INTEGER NOT NULL,
  "id_workers" INTEGER NOT NULL,
  PRIMARY KEY ("id_customers", "id_filter", "id_workers")
);

CREATE INDEX "idx_customers_filter__id_filter" ON "customers_filter" ("id_filter");

CREATE INDEX "idx_customers_filter__id_workers" ON "customers_filter" ("id_workers");

ALTER TABLE "customers_filter" ADD CONSTRAINT "fk_customers_filter__id_customers" FOREIGN KEY ("id_customers") REFERENCES "customers" ("id") ON DELETE CASCADE;

ALTER TABLE "customers_filter" ADD CONSTRAINT "fk_customers_filter__id_filter" FOREIGN KEY ("id_filter") REFERENCES "filter" ("id") ON DELETE CASCADE;

ALTER TABLE "customers_filter" ADD CONSTRAINT "fk_customers_filter__id_workers" FOREIGN KEY ("id_workers") REFERENCES "workers" ("id") ON DELETE CASCADE