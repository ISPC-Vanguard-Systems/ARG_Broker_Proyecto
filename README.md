<img src="/header.png" width='100%'>
<h2 align='center' >📍 Introducción</h2>
<br>
El propósito fundamental de ARGBroker Demo radica en el desarrollo de una aplicación de simulación diseñada específicamente para la empresa tecnológica Vanguard Systems. Esta empresa, habiéndose registrado como corredora de bolsa, busca ofrecer a sus clientes una plataforma innovadora que sirva como puente entre los inversores y la vibrante actividad de la Bolsa de Valores de Buenos Aires (MERVAL).
<br>
La aplicación simuladora actúa como un intermediario virtual, proporcionando a los usuarios una experiencia realista de compra y venta de acciones en un entorno controlado y seguro. Mediante el uso de esta plataforma, los inversores pueden explorar el mundo de las inversiones en el mercado de valores sin arriesgar capital real.
<br>

Con ARGBroker Demo, Vanguard Systems implementa una aplicación de consola diseñada para gestionar un portafolio de inversiones, permitiendo a los usuarios registrar nuevas cuentas de inversores, iniciar sesión y realizar diversas operaciones de compra y venta de activos. El desarrollo sigue una metodología de Desarrollo Guiado por Pruebas (TDD) y aplica las 4 reglas de diseño simple de Kent Beck, priorizando claridad y facilidad de mantenimiento.
<br>
<h2 align='center' >📍 Funcionalidades principales</h2>
<br>
 <h3> Registro e Inicio de Sesión</h3>
•	Registro de un nuevo inversor con datos personales: nombre, apellido, CUIL, email y contraseña. <br>
•	Inicio de sesión seguro y validación de credenciales. <br>
•	Opcional: Recuperación de contraseña y bloqueo de la cuenta después de tres intentos fallidos de inicio de sesión. <br>
  <h3>  Operaciones Disponibles en el Menú </h3>
•	Visualización de la Cuenta: Permite al usuario ver el saldo de su cuenta, el total invertido y el rendimiento total de su portafolio. <br>
•	Listado de Activos en el Portafolio: Muestra los activos en propiedad, incluyendo el nombre de la empresa, cantidad de acciones, valores de cotización (precio actual para compra y venta) y rendimiento de cada activo. <br>
•	Operaciones de Compra/Venta de Acciones: Permite realizar transacciones con las siguientes consideraciones: <br>
o	Validaciones como la disponibilidad de fondos y existencias de acciones. <br>
o	Registro de cada transacción, incluyendo la comisión del bróker. <br>
o	Actualización automática del portafolio, saldo y total invertido. <br>
<h2 align='center' >📍 Convenciones de Nomenclatura</h2>
Para asegurar la consistencia y legibilidad del código, se siguen las siguientes convenciones de nomenclatura: <br>
•	Archivos y Directorios<br>
o	Archivos Python: Formato en snake_case en minúsculas. Ejemplo: main.py, interface_dao.py. <br>
o	Directorios: Nombres en minúsculas sin espacios ni caracteres especiales. Ejemplo: accesos, clases. <br>
•	Clases <br>
o	Formato PascalCase para los nombres de clases. Ejemplo: Usuario, Transaccion. <br>
•	Funciones y Métodos <br>
o	Formato snake_case en minúsculas, comenzando la primera palabra con un verbo en infinitivo. Ejemplo: ejecutar_query, iniciar_transaccion. <br>
•	Variables<br>
o	Formato snake_case en minúsculas. Ejemplo: saldo, rendimiento_acumulado. <br>
•	Constantes<br>
o	Formato snake_case en mayúsculas. Ejemplo: INTENTOS. <br>
Este proyecto está diseñado para crecer y escalar, permitiendo la adición de nuevas funcionalidades y la adaptación a futuras necesidades de los usuarios. <br>
<div align="center"> 
 <h2 align='center' >📍 Requerimientos del Diseño de la Base de Datos</h2>
1.	Modelo Relacional <br>
o	Se ha diseñado un modelo relacional que incluye las entidades principales del sistema, integrando mejoras basadas en las devoluciones anteriores. El modelo soporta: <br>
	Un registro histórico de las cotizaciones de acciones, permitiendo un seguimiento detallado de los valores de mercado. <br>
	Registro de todas las transacciones de compra y venta de activos, incluyendo las comisiones del bróker para asegurar precisión en los cálculos financieros. <br>
2.	Creación de la Base de Datos <br>
o	Se proporcionan scripts DDL (Data Definition Language) que permiten la creación de la base de datos con todas sus tablas replicando el modelo relacional. <br>
3.	Inserción de Datos Iniciales <br>
o	Sentencias DML (Data Manipulation Language) INSERT están disponibles para poblar la base de datos con datos iniciales, permitiendo una configuración básica de prueba. <br>
4.	Actualización de Datos <br>
o	Se incluyen al menos cinco sentencias de tipo UPDATE para la modificación de datos ya existentes, permitiendo actualizar información clave de manera controlada. <br>
5.	Consultas de Selección de Datos <br>
o	Se han desarrollado cinco consultas de tipo SELECT, diseñadas para obtener información relevante y generar reportes útiles de la base de datos. <br>
6.	Consultas Multitabla <br>
o	Se proporcionan tres consultas multitabla con su respectiva explicación del caso de uso. Estas consultas permiten obtener información valiosa para el análisis del portafolio y la gestión de transacciones. Cada consulta incluye una breve descripción de su propósito. <br><br>
|Participantes|Correo electrónico|Perfil|
|:---:|:---:|:---:|
|**Aldo Minoldo**|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:minoldoaldo@gmail.com)|[![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AAMinoldo)|
|**Nicolas Minoldo**|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:minoldonico@gmail.com)| [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NicolasMinoldo)|
|**Fabricio Quiroga**|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fabripingui@gmail.com)| [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fabricioquiroga)|
|**Patricio Rodriguez**|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](Mailto:rpatricioesteban@gmail.com)| [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/1PatoRod)|
|**Maxi Scarpatti**|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:maxi.scarpatti@gmail.com)| [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MaxiScarpatti)|
|**Rodrigo Valdez**|[![Correo](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fori2001@hotmail.com)| [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MrForii)|
|**Roxana Vilchez**|[![LinkedIn](https://img.shields.io/badge/correo-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vilchezro33@hotmail.com)| [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Roxana333)|

</div>
<br>
<h2 align='center' >📍 Entregables Segunda Etapa</h2>

<h3 align='center' >🚀 <a href="https://github.com/ISPC-Vanguard-Systems/ARG_Broker_Proyecto/blob/main/app/base_de_datos/EER_broker.pdf" align='center'>Diagrama ER Base de Datos</a></h3>

<h3 align='center' >🚀 <a href="https://github.com/ISPC-Vanguard-Systems/ARG_Broker_Proyecto/blob/main/app/base_de_datos/scrip_base_de_datos_broker.tex" align='center'>Script con las consultas Base de Datos </a></h3>
