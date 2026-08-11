PIXHAWK_UART = "/dev/serial0"   
PIXHAWK_BAUD = 921600           

LIDAR_USE_UART = True
LIDAR_UART_PORT = "/dev/ttyUSB0"
LIDAR_UART_BAUD = 115200
LIDAR_I2C_BUS = 1
LIDAR_I2C_ADDR = 0x10           

ADC_SPI_BUS = 0
ADC_SPI_DEVICE = 0
ADC_CHANNEL_GAS = 0             
MQ2_CLEAN_AIR_VOLT = 0.2        
MQ2_GAS_THRESHOLD = 0.6         


RGB_R_PIN = 17
RGB_G_PIN = 27
RGB_B_PIN = 22
PIEZO_PIN = 18

ROBOFLOW_WORKSPACES = {
    "fire_smoke_human": {
        "project": "fire-smoke-and-human-detector",  
        "workspace": "spyrobot",
        "version": 1
    },
    "rubble": {
        "project": "rubble-detection",                
        "workspace": "rubble-project",
        "version": 6
    },
    "road_obstacle": {
        "project": "road-obstacle-detection",         
        "workspace": "project-ganpo",
        "version": 1
    },
    "thermal_human": {
        "project": "thermal-human-detection-from-uav",
        "workspace": "thermal-disasters-project",
        "version": 1
    }
}


RGB_CAMERA_INDEX = 0       
THERMAL_CAMERA_INDEX = 1   
