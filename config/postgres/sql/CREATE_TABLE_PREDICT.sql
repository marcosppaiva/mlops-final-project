CREATE TABLE prediction(
	id serial primary key,
	district varchar(255),
	property_type varchar(30),
	bathroom int,
	metric float,
	rooms int,
	energy_certify varchar(20),
	condition varchar(50),
	price_predicted float,
	model_version varchar(300),
	created_time timestamp DEFAULT CURRENT_TIMESTAMP
);
