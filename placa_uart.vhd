COMPONENT uart
	GENERIC (
		CLOCK_FREQUENCY : INTEGER := 50000000; -- Frequência CLOCK_UART
		BAUDRATE_RX : INTEGER := 115200; -- taxa de recepção
		BAUDRATE_TX : INTEGER := 115200 ); -- taxa de transmissão
	PORT
	(
		CLOCK_SAMPLE : IN STD_LOGIC;
		CLOCK_UART : IN STD_LOGIC;
		serial_rx : IN STD_LOGIC;
		start_tx : IN STD_LOGIC;
		serial_write : IN STD_LOGIC_VECTOR(7 DOWNTO 0);
		busy_rx : OUT STD_LOGIC;		
		busy_tx : OUT STD_LOGIC;
		valid_rx : OUT STD_LOGIC;
		serial_tx : OUT STD_LOGIC;
		serial_read : OUT STD_LOGIC_VECTOR(7 DOWNTO 0)
	);
END COMPONENT;
