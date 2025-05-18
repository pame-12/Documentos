-- Base de datos
CREATE DATABASE IF NOT EXISTS plataforma_empleos;
USE plataforma_empleos;

-- Tabla: Candidatos
CREATE TABLE candidatos (
    id_candidato INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    correo VARCHAR(150) UNIQUE,
    contraseña VARCHAR(255),
    telefono VARCHAR(20),
    direccion TEXT,
    ciudad VARCHAR(100),
    objetivo_profesional TEXT,
    disponibilidad VARCHAR(50),
    foto VARCHAR(255),
    cv_pdf VARCHAR(255)
);

-- Tabla: Formación Académica
CREATE TABLE formacion (
    id_formacion INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    institucion VARCHAR(150),
    titulo VARCHAR(150),
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE
);

-- Tabla: Experiencia Laboral
CREATE TABLE experiencia (
    id_experiencia INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    empresa VARCHAR(150),
    puesto VARCHAR(150),
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT,
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE
);

-- Tabla: Habilidades
CREATE TABLE habilidades (
    id_habilidad INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    nombre VARCHAR(100),
    nivel ENUM('Básico', 'Intermedio', 'Avanzado'),
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE
);

-- Tabla: Idiomas
CREATE TABLE idiomas (
    id_idioma INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    idioma VARCHAR(100),
    nivel ENUM('Básico', 'Intermedio', 'Avanzado'),
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE
);

-- Tabla: Redes Profesionales
CREATE TABLE redes_profesionales (
    id_red INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    tipo VARCHAR(50),
    url VARCHAR(255),
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE
);

-- Tabla: Referencias
CREATE TABLE referencias (
    id_referencia INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    nombre VARCHAR(100),
    contacto VARCHAR(150),
    descripcion TEXT,
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE
);

-- Tabla: Empresas
CREATE TABLE empresas (
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(150),
    correo VARCHAR(150) UNIQUE,
    contraseña VARCHAR(255),
    direccion TEXT
);

-- Tabla: Ofertas de Empleo
CREATE TABLE ofertas (
    id_oferta INT AUTO_INCREMENT PRIMARY KEY,
    id_empresa INT,
    titulo_puesto VARCHAR(150),
    descripcion TEXT,
    requisitos TEXT,
    fecha_publicacion DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE
);

-- Tabla: Aplicaciones a Ofertas
CREATE TABLE aplicaciones (
    id_aplicacion INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    id_oferta INT,
    fecha_aplicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato) ON DELETE CASCADE,
    FOREIGN KEY (id_oferta) REFERENCES ofertas(id_oferta) ON DELETE CASCADE,
    UNIQUE (id_candidato, id_oferta)
);












