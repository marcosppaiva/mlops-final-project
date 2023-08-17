CREATE TABLE drift_metrics(

	id serial primary key,
	drift_score float,
	drift_detected bool,
	number_of_columns int,
	number_of_drifted_columns int,
	share_of_missing_values float,
	created_time timestamp DEFAULT CURRENT_TIMESTAMP
);
