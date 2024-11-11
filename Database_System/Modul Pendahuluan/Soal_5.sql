alter table bandara_penerbangan
drop foreign key bandara_penerbangan_ibfk_1;

alter table bandara
drop primary key;

alter table bandara
add primary key (Kode_IATA);

alter table bandara_penerbangan
modify column Bandara_ID char(3);

alter table bandara_penerbangan
add foreign key (Bandara_ID) references bandara(Kode_IATA)
    on delete cascade
    on update cascade;

INSERT INTO `bandara_penerbangan`(`Bandara_ID`, `Penerbangan_ID`) 
VALUES 
('CGK', 'FL0001'),
('DPS', 'FL0002'),
('HND', 'FL0004');