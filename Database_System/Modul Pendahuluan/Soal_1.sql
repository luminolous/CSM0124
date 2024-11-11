create table Bandara (
    ID int primary key,
    Nama varchar(255),
    Kota varchar(255),
    Negara varchar(255),
    Kode_IATA char(3)
);

create table Maskapai (
    ID char(6) primary key,
    Nama varchar(255),
    Negara_Asal varchar(255)
);

create table Bagasi (
    ID int primary key,
    Berat int,
    Ukuran varchar(5),
    Warna varchar(255),
    Jenis varchar(255)
);

create table Pesawat (
    ID char(6) primary key,
    Model varchar(255),
    Kapasitas int,
    Tahun_produksi char(4),
    Status_pesawat varchar(50),
    Maskapai_ID char(6),
    foreign key (Maskapai_ID) references Maskapai(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

create table Penumpang (
    NIK char(16) primary key,
    Nama varchar(255),
    Tanggal_lahir date,
    Alamat varchar(255),
    No_telepon varchar(13),
    Jenis_kelamin char(1),
    Kewarganegaraan varchar(255),
    Bagasi_ID int,
    foreign key (Bagasi_ID) references Bagasi(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

create table Penerbangan (
    ID char(6) primary key,
    Waktu_keberangkatan datetime,
    Waktu_sampai datetime,
    Status_penerbangan varchar(50),
    Pesawat_ID char(6),
    foreign key (Pesawat_ID) references Pesawat(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

create table Tiket (
    ID char(6) primary key,
    Nomor_kursi char(3),
    Harga int,
    Waktu_pembelian datetime,
    Kelas_penerbangan varchar(50),
    Penumpang_NIK char(16),
    Penerbangan_ID char(6),
    foreign key (Penumpang_NIK) references Penumpang(NIK)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    foreign key (Penerbangan_ID) references Penerbangan(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

create table Bandara_penerbangan (
    Bandara_ID INT,
    Penerbangan_ID char(6),
    primary key (Bandara_ID, Penerbangan_ID),
    foreign key (Bandara_ID) references Bandara(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    foreign key (Penerbangan_ID) references Penerbangan(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

