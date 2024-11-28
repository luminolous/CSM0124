insert into pegawai
values 
('PG0001', '1234567890123451', 'Budi Sumanto', 'L', 32, '081156781298'),
('PG0002', '1234567890129164', 'William Santoso', 'L', 25, '082267892309'),
('PG0003', '1234567890124577', 'Bronya', 'P', 23, '083378903410'),
('PG0004', '1234567890121111', 'Rina Maharani', 'P', 28, '0844890145212'),
('PG0005', '1234567890128678', 'Ujang', 'L', 30, '0855901256329');

insert into penyewa
values
('PY0001', 'Beyonce', '081255551243'),
('PY0002', 'Walter Jones', '0823666656872'),
('PY0003', 'Gepard Landau', '0834777790211'),
('PY0004', 'Arataki Itto', '0856888834652'),
('PY0005', 'Suparjo', '087899997809'),
('PY0006', 'Kevin Miller', '088911118462');

insert into tim_peminjam
values 
('T00001', 'Honkai Sport Club', '21'),
('T00002', 'Dragon Warriors', '15'),
('T00003', 'Phoenix Squad', '17');

insert into lapangan
values 
('LP0001', 'Lapangan Basket A', 'Jl. Cempaka Timur 23', 'Basket', 420, 150000.00),
('LP0002', 'Lapangan Basket B', 'Jl. Mawar 77', 'Basket', 420, 150000.00),
('LP0003', 'Lapangan Futsal A', 'Jl. Cempaka Barat 21', 'Futsal', 1050, 150000.00),
('LP0004', 'Lapangan Badminton A', 'Jl. Merpati 18', 'Badminton', 81.74, 75000.00),
('LP0005', 'Lapangan Badminton B', 'Jl. Merpati 18', 'Badminton', 81.74, 75000.00),
('LP0006', 'Lapangan Voli A', 'Jl. Ikan Kembung 3', 'Voli', 162, 120000.00),
('LP0007', 'Lapangan Voli B', 'Jl. Ikan Mujaer 53','Voli', 162, 120000.00);

insert into cleaning_service
values 
('CS0001', 'Anto Seno', '089911223344', 3),
('CS0002', 'Joko Sutrisno', '0899123456789', 5),
('CS0003', 'Kartika Sari', '0833665589767', 6),
('CS0004', 'Dewi Sara', '084411119993', 1);

insert into tingkatan_membership
values 
('TM0001', 'Bronze', 10000.00, 2000.00),
('TM0002', 'Silver', 20000.00, 5000.00),
('TM0003', 'Gold', 25000.00, 7500.00);

insert into kartu_membership
values 
('MB0001', '1234567890199203', 'Jl. Cempaka Pusat 88', '2023-11-10', 1, 'PY0003', 'TM0002'),
('MB0002', '1234567890736152', 'Jl. Mangrove 73', '2024-10-13', 2, 'PY0004', 'TM0002'),
('MB0003', '1234567890874524', 'Jl. Pisang Hijau 99', '2024-11-01', 2, 'PY0001', 'TM0003');

insert into transaksi
values 
('TR0001', '2023-11-10', '2023-11-10' , '10:00:00' , 3, 1, 470000.00, 'Cash', 'PG0003', 'PY0003', 'LP0001', 'T00001'),
('TR0002', '2024-03-30', '2024-04-01', '08:00:00', 4, 0, 480000.00, 'Transfer Bank', 'PG0002', 'PY0002', 'LP0007', 'T00003'),
('TR0003', '2024-10-13', '2024-10-20', '20:00:00', 2, 1, 320000.00, 'Kartu Kredit', 'PG0004', 'PY0004', 'LP0003', 'T00002'),
('TR0004', '2024-11-01', '2024-11-20', '20:00:00', 2, 0, 295000.00, 'Kartu Kredit', 'PG0004', 'PY0004', 'LP0003', 'T00002'),
('TR0005', '2024-11-01', '2024-11-11', '09:00:00', 6, 1, 925000.00, 'Transfer Bank', 'PG0002', 'PY0001', 'LP0002', 'T00003');

insert into cs_lapangan 
values 
('LP0001', 'CS0004'),
('LP0001', 'CS0003'),
('LP0002', 'CS0002'),
('LP0003', 'CS0001'),
('LP0004', 'CS0001'),
('LP0005', 'CS0003'),
('LP0005', 'CS0004'),
('LP0006', 'CS0002'),
('LP0007', 'CS0003');

