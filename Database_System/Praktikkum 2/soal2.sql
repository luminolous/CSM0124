create table tingkatan_membership (
    tm_id char(6) primary key,
    tm_nama varchar(20) not null,
    tm_biaya_pendaftaran float(2) not null,
    tm_potongan_harga float(2) not null
);

ALTER TABLE kartu_membership
ADD COLUMN tingkatan_id char(6) not null;

ALTER TABLE kartu_membership
ADD CONSTRAINT fk_tingkatan_id
FOREIGN KEY (tingkatan_id) REFERENCES tingkatan_membership(tm_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
