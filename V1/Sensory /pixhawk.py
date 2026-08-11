import asyncio
from mavsdk import System
from config import PIXHAWK_UART, PIXHAWK_BAUD

class PixhawkInterface:
    def __init__(self):
        self.drone = System()

    async def connect(self):

        uri = f"serial://{PIXHAWK_UART}:{PIXHAWK_BAUD}"
        await self.drone.connect(system_address=uri)

        async for state in self.drone.core.connection_state():
            if state.is_connected:
                print("Pixhawk connected")
                break

    async def arm_and_takeoff(self, altitude=10.0):
        print("Arming...")
        await self.drone.action.arm()
        print("Taking off...")
        await self.drone.action.takeoff()
        await asyncio.sleep(10)
        await self.drone.action.goto_location(
            latitude_deg=0.0, longitude_deg=0.0,
            absolute_altitude_m=altitude, yaw_deg=0.0
        )

    async def land(self):
        print("Landing...")
        await self.drone.action.land()

    async def set_rc_override(self, roll, pitch, yaw, throttle):

        pass

    async def get_telemetry(self):
        async for pos in self.drone.telemetry.position():
            return pos

if __name__ == "__main__":
    async def main():
        pix = PixhawkInterface()
        await pix.connect()
        pos = await pix.get_telemetry()
        print(pos)

    asyncio.run(main())
