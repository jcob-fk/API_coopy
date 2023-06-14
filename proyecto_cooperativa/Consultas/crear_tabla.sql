/****** Script for SelectTopNRows command from SSMS  ******/
CREATE TABLE Clientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    genero VARCHAR(10),
    correo_electronico VARCHAR(100),
    direccion VARCHAR(200),
    ciudad VARCHAR(50),
    estado VARCHAR(50),
    pais VARCHAR(50),
    codigo_postal VARCHAR(10),
    telefono VARCHAR(20),
    saldo_ahorros DECIMAL(18,2)
);

INSERT INTO Clientes (nombre, apellido, fecha_nacimiento, genero, correo_electronico, direccion, ciudad, estado, pais, codigo_postal, telefono, saldo_ahorros)
VALUES 
    ('Ana', 'L�pez', '1989-05-15', 'Femenino', 'ana.lopez@gmail.com', 'Calle 456', 'Ciudad de M�xico', 'Ciudad de M�xico', 'M�xico', '12345', '555-111-2222', 12000.00),
    ('Jorge', 'Mart�nez', '1978-09-27', 'Masculino', 'jorge.martinez@gmail.com', 'Avenida 789', 'Monterrey', 'Nuevo Le�n', 'M�xico', '67890', '555-222-3333', 8000.00),
    ('Karla', 'Garc�a', '1995-06-07', 'Femenino', 'karla.garcia@gmail.com', 'Calle 1011', 'Guadalajara', 'Jalisco', 'M�xico', '13579', '555-333-4444', 5000.00),
    ('Miguel', 'Hern�ndez', '1984-03-21', 'Masculino', 'miguel.hernandez@gmail.com', 'Avenida 1213', 'Tijuana', 'Baja California', 'M�xico', '24680', '555-444-5555', 2000.00),
    ('Sof�a', 'P�rez', '2000-12-05', 'Femenino', 'sofia.perez@gmail.com', 'Calle 1415', 'Canc�n', 'Quintana Roo', 'M�xico', '36912', '555-555-6666', 4000.00),
    ('Luis', 'Rodr�guez', '1975-07-12', 'Masculino', 'luis.rodriguez@gmail.com', 'Avenida 1617', 'Ciudad Ju�rez', 'Chihuahua', 'M�xico', '48152', '555-666-7777', 10000.00),
    ('Fernanda', 'S�nchez', '1999-02-01', 'Femenino', 'fernanda.sanchez@gmail.com', 'Calle 1819', 'Toluca', 'M�xico', 'M�xico', '75310', '555-777-8888', 7000.00),
    ('Carlos', 'Gonz�lez', '1988-11-23', 'Masculino', 'carlos.gonzalez@gmail.com', 'Avenida 2021', 'Veracruz', 'M�xico', 'M�xico', '96543', '555-888-9999', 3000.00),
    ('Paula', 'Mart�nez', '1991-08-17', 'Femenino', 'paula.martinez@gmail.com', 'Calle 2223', 'Hermosillo', 'Sonora', 'M�xico', '82736', '555-999-0000', 6000.00),
    ('Mar�a', 'Guti�rrez', '1992-01-25', 'Femenino', 'maria.gutierrez@gmail.com', 'Calle 2627', 'Culiac�n', 'Sinaloa', 'M�xico', '72000', '555-000-1111', 9000.00);

	UPDATE Clientes SET pais = 'Mexico';