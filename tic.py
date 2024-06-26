import random
import datetime
colors = ['"#0B24FB"', '"#29FD2E",' '"#32FDFC"', '"#FB2FFC"', '"#FCFD45"', '"#FF0000"']

def get_random_color():
    return random.choice(colors)

random_color_1 = get_random_color()
colors.remove(random_color_1)

random_color_2 = get_random_color()
colors.remove(random_color_2)

board_color = '"#D9D9D9"'
board_string = f"""    
    <line x1="34" y1="8" x2="34" y2="90" stroke={board_color} stroke-dasharray="1" />
    <line x1="62" y1="8" x2="62" y2="90" stroke={board_color} stroke-dasharray="1" />
    <line x1="8" y1="34" x2="90" y2="34" stroke={board_color} stroke-dasharray="1" />
    <line x1="8" y1="62" x2="90" y2="62" stroke={board_color} stroke-dasharray="1" />

    """
punk_string = f"""
<svg viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" transform="translate(0.5 0.5)" fill="black" />
    <defs>
        <g id="punk_main" transform="scale(0.25)">
            <path d="M32.5 95.5H35.5V92.5H32.5V95.5Z"  />
            <path d="M36.5 95.5H39.5V92.5H36.5V95.5Z"  />
            <path d="M40.5 95.5H43.5V92.5H40.5V95.5Z"  />
            <path d="M44.5 95.5H47.5V92.5H44.5V95.5Z"  />
            <path d="M48.5 95.5H51.5V92.5H48.5V95.5Z"  />
            <path d="M52.5 95.5H55.5V92.5H52.5V95.5Z"  />
            <path d="M56.5 95.5H59.5V92.5H56.5V95.5Z"  />
            <path d="M60.5 95.5H63.5V92.5H60.5V95.5Z"  />
            <path d="M24.5 91.5H27.5V88.5H24.5V91.5Z"  />
            <path d="M28.5 91.5H31.5V88.5H28.5V91.5Z"  />
            <path d="M32.5 91.5H35.5V88.5H32.5V91.5Z"  />
            <path d="M36.5 91.5H39.5V88.5H36.5V91.5Z"  />
            <path d="M40.5 91.5H43.5V88.5H40.5V91.5Z"  />
            <path d="M44.5 91.5H47.5V88.5H44.5V91.5Z"  />
            <path d="M48.5 91.5H51.5V88.5H48.5V91.5Z"  />
            <path d="M52.5 91.5H55.5V88.5H52.5V91.5Z"  />
            <path d="M56.5 91.5H59.5V88.5H56.5V91.5Z"  />
            <path d="M60.5 91.5H63.5V88.5H60.5V91.5Z"  />
            <path d="M64.5 91.5H67.5V88.5H64.5V91.5Z"  />
            <path d="M68.5 91.5H71.5V88.5H68.5V91.5Z"  />
            <path d="M16.5 87.5H19.5V84.5H16.5V87.5Z"  />
            <path d="M20.5 87.5H23.5V84.5H20.5V87.5Z"  />
            <path d="M24.5 87.5H27.5V84.5H24.5V87.5Z"  />
            <path d="M28.5 87.5H31.5V84.5H28.5V87.5Z"  />
            <path d="M32.5 87.5H35.5V84.5H32.5V87.5Z"  />
            <path d="M36.5 87.5H39.5V84.5H36.5V87.5Z"  />
            <path d="M40.5 87.5H43.5V84.5H40.5V87.5Z"  />
            <path d="M44.5 87.5H47.5V84.5H44.5V87.5Z"  />
            <path d="M48.5 87.5H51.5V84.5H48.5V87.5Z"  />
            <path d="M52.5 87.5H55.5V84.5H52.5V87.5Z"  />
            <path d="M56.5 87.5H59.5V84.5H56.5V87.5Z"  />
            <path d="M60.5 87.5H63.5V84.5H60.5V87.5Z"  />
            <path d="M64.5 87.5H67.5V84.5H64.5V87.5Z"  />
            <path d="M68.5 87.5H71.5V84.5H68.5V87.5Z"  />
            <path d="M72.5 87.5H75.5V84.5H72.5V87.5Z"  />
            <path d="M76.5 87.5H79.5V84.5H76.5V87.5Z"  />
            <path d="M12.5 83.5H15.5V80.5H12.5V83.5Z"  />
            <path d="M16.5 83.5H19.5V80.5H16.5V83.5Z"  />
            <path d="M20.5 83.5H23.5V80.5H20.5V83.5Z"  />
            <path d="M24.5 83.5H27.5V80.5H24.5V83.5Z"  />
            <path d="M28.5 83.5H31.5V80.5H28.5V83.5Z"  />
            <path d="M32.5 83.5H35.5V80.5H32.5V83.5Z"  />
            <path d="M36.5 83.5H39.5V80.5H36.5V83.5Z"  />
            <path d="M40.5 83.5H43.5V80.5H40.5V83.5Z"  />
            <path d="M44.5 83.5H47.5V80.5H44.5V83.5Z"  />
            <path d="M48.5 83.5H51.5V80.5H48.5V83.5Z"  />
            <path d="M52.5 83.5H55.5V80.5H52.5V83.5Z"  />
            <path d="M56.5 83.5H59.5V80.5H56.5V83.5Z"  />
            <path d="M60.5 83.5H63.5V80.5H60.5V83.5Z"  />
            <path d="M64.5 83.5H67.5V80.5H64.5V83.5Z"  />
            <path d="M68.5 83.5H71.5V80.5H68.5V83.5Z"  />
            <path d="M72.5 83.5H75.5V80.5H72.5V83.5Z"  />
            <path d="M76.5 83.5H79.5V80.5H76.5V83.5Z"  />
            <path d="M80.5 83.5H83.5V80.5H80.5V83.5Z"  />
            <path d="M8.5 79.5H11.5V76.5H8.5V79.5Z"  />
            <path d="M12.5 79.5H15.5V76.5H12.5V79.5Z"  />
            <path d="M16.5 79.5H19.5V76.5H16.5V79.5Z"  />
            <path d="M20.5 79.5H23.5V76.5H20.5V79.5Z"  />
            <path d="M24.5 79.5H27.5V76.5H24.5V79.5Z"  />
            <path d="M28.5 79.5H31.5V76.5H28.5V79.5Z"  />
            <path d="M32.5 79.5H35.5V76.5H32.5V79.5Z"  />
            <path d="M36.5 79.5H39.5V76.5H36.5V79.5Z"  />
            <path d="M40.5 79.5H43.5V76.5H40.5V79.5Z"  />
            <path d="M44.5 79.5H47.5V76.5H44.5V79.5Z"  />
            <path d="M48.5 79.5H51.5V76.5H48.5V79.5Z"  />
            <path d="M52.5 79.5H55.5V76.5H52.5V79.5Z"  />
            <path d="M56.5 79.5H59.5V76.5H56.5V79.5Z"  />
            <path d="M60.5 79.5H63.5V76.5H60.5V79.5Z"  />
            <path d="M64.5 79.5H67.5V76.5H64.5V79.5Z"  />
            <path d="M68.5 79.5H71.5V76.5H68.5V79.5Z"  />
            <path d="M72.5 79.5H75.5V76.5H72.5V79.5Z"  />
            <path d="M76.5 79.5H79.5V76.5H76.5V79.5Z"  />
            <path d="M80.5 79.5H83.5V76.5H80.5V79.5Z"  />
            <path d="M84.5 79.5H87.5V76.5H84.5V79.5Z"  />
            <path d="M8.5 75.5H11.5V72.5H8.5V75.5Z"  />
            <path d="M12.5 75.5H15.5V72.5H12.5V75.5Z"  />
            <path d="M16.5 75.5H19.5V72.5H16.5V75.5Z"  />
            <path d="M20.5 75.5H23.5V72.5H20.5V75.5Z"  />
            <path d="M24.5 75.5H27.5V72.5H24.5V75.5Z"  />
            <path d="M28.5 75.5H31.5V72.5H28.5V75.5Z"  />
            <path d="M32.5 75.5H35.5V72.5H32.5V75.5Z"  />
            <path d="M36.5 75.5H39.5V72.5H36.5V75.5Z"  />
            <path d="M40.5 75.5H43.5V72.5H40.5V75.5Z"  />
            <path d="M44.5 75.5H47.5V72.5H44.5V75.5Z"  />
            <path d="M48.5 75.5H51.5V72.5H48.5V75.5Z"  />
            <path d="M52.5 75.5H55.5V72.5H52.5V75.5Z"  />
            <path d="M56.5 75.5H59.5V72.5H56.5V75.5Z"  />
            <path d="M60.5 75.5H63.5V72.5H60.5V75.5Z"  />
            <path d="M64.5 75.5H67.5V72.5H64.5V75.5Z"  />
            <path d="M68.5 75.5H71.5V72.5H68.5V75.5Z"  />
            <path d="M72.5 75.5H75.5V72.5H72.5V75.5Z"  />
            <path d="M76.5 75.5H79.5V72.5H76.5V75.5Z"  />
            <path d="M80.5 75.5H83.5V72.5H80.5V75.5Z"  />
            <path d="M84.5 75.5H87.5V72.5H84.5V75.5Z"  />
            <path d="M4.5 71.5H7.5V68.5H4.5V71.5Z"  />
            <path d="M8.5 71.5H11.5V68.5H8.5V71.5Z"  />
            <path d="M12.5 71.5H15.5V68.5H12.5V71.5Z"  />
            <path d="M16.5 71.5H19.5V68.5H16.5V71.5Z"  />
            <path d="M20.5 71.5H23.5V68.5H20.5V71.5Z"  />
            <path d="M24.5 71.5H27.5V68.5H24.5V71.5Z"  />
            <path d="M28.5 71.5H31.5V68.5H28.5V71.5Z"  />
            <path d="M32.5 71.5H35.5V68.5H32.5V71.5Z"  />
            <path d="M36.5 71.5H39.5V68.5H36.5V71.5Z"  />
            <path d="M40.5 71.5H43.5V68.5H40.5V71.5Z"  />
            <path d="M44.5 71.5H47.5V68.5H44.5V71.5Z"  />
            <path d="M48.5 71.5H51.5V68.5H48.5V71.5Z"  />
            <path d="M52.5 71.5H55.5V68.5H52.5V71.5Z"  />
            <path d="M56.5 71.5H59.5V68.5H56.5V71.5Z"  />
            <path d="M60.5 71.5H63.5V68.5H60.5V71.5Z"  />
            <path d="M64.5 71.5H67.5V68.5H64.5V71.5Z"  />
            <path d="M68.5 71.5H71.5V68.5H68.5V71.5Z"  />
            <path d="M72.5 71.5H75.5V68.5H72.5V71.5Z"  />
            <path d="M76.5 71.5H79.5V68.5H76.5V71.5Z"  />
            <path d="M80.5 71.5H83.5V68.5H80.5V71.5Z"  />
            <path d="M84.5 71.5H87.5V68.5H84.5V71.5Z"  />
            <path d="M88.5 71.5H91.5V68.5H88.5V71.5Z"  />
            <path d="M4.5 67.5H7.5V64.5H4.5V67.5Z"  />
            <path d="M8.5 67.5H11.5V64.5H8.5V67.5Z"  />
            <path d="M12.5 67.5H15.5V64.5H12.5V67.5Z"  />
            <path d="M16.5 67.5H19.5V64.5H16.5V67.5Z"  />
            <path d="M20.5 67.5H23.5V64.5H20.5V67.5Z"  />
            <path d="M24.5 67.5H27.5V64.5H24.5V67.5Z"  />
            <path d="M28.5 67.5H31.5V64.5H28.5V67.5Z"  />
            <path d="M32.5 67.5H35.5V64.5H32.5V67.5Z"  />
            <path d="M36.5 67.5H39.5V64.5H36.5V67.5Z"  />
            <path d="M40.5 67.5H43.5V64.5H40.5V67.5Z"  />
            <path d="M44.5 67.5H47.5V64.5H44.5V67.5Z"  />
            <path d="M48.5 67.5H51.5V64.5H48.5V67.5Z"  />
            <path d="M52.5 67.5H55.5V64.5H52.5V67.5Z"  />
            <path d="M56.5 67.5H59.5V64.5H56.5V67.5Z"  />
            <path d="M60.5 67.5H63.5V64.5H60.5V67.5Z"  />
            <path d="M64.5 67.5H67.5V64.5H64.5V67.5Z"  />
            <path d="M68.5 67.5H71.5V64.5H68.5V67.5Z"  />
            <path d="M72.5 67.5H75.5V64.5H72.5V67.5Z"  />
            <path d="M76.5 67.5H79.5V64.5H76.5V67.5Z"  />
            <path d="M80.5 67.5H83.5V64.5H80.5V67.5Z"  />
            <path d="M84.5 67.5H87.5V64.5H84.5V67.5Z"  />
            <path d="M88.5 67.5H91.5V64.5H88.5V67.5Z"  />
            <path d="M0.5 63.5H3.5V60.5H0.5V63.5Z"  />
            <path d="M4.5 63.5H7.5V60.5H4.5V63.5Z"  />
            <path d="M8.5 63.5H11.5V60.5H8.5V63.5Z"  />
            <path d="M12.5 63.5H15.5V60.5H12.5V63.5Z"  />
            <path d="M16.5 63.5H19.5V60.5H16.5V63.5Z"  />
            <path d="M20.5 63.5H23.5V60.5H20.5V63.5Z"  />
            <path d="M24.5 63.5H27.5V60.5H24.5V63.5Z"  />
            <path d="M28.5 63.5H31.5V60.5H28.5V63.5Z"  />
            <path d="M32.5 63.5H35.5V60.5H32.5V63.5Z"  />
            <path d="M36.5 63.5H39.5V60.5H36.5V63.5Z"  />
            <path d="M40.5 63.5H43.5V60.5H40.5V63.5Z"  />
            <path d="M44.5 63.5H47.5V60.5H44.5V63.5Z"  />
            <path d="M48.5 63.5H51.5V60.5H48.5V63.5Z"  />
            <path d="M52.5 63.5H55.5V60.5H52.5V63.5Z"  />
            <path d="M56.5 63.5H59.5V60.5H56.5V63.5Z"  />
            <path d="M60.5 63.5H63.5V60.5H60.5V63.5Z"  />
            <path d="M64.5 63.5H67.5V60.5H64.5V63.5Z"  />
            <path d="M68.5 63.5H71.5V60.5H68.5V63.5Z"  />
            <path d="M72.5 63.5H75.5V60.5H72.5V63.5Z"  />
            <path d="M76.5 63.5H79.5V60.5H76.5V63.5Z"  />
            <path d="M80.5 63.5H83.5V60.5H80.5V63.5Z"  />
            <path d="M84.5 63.5H87.5V60.5H84.5V63.5Z"  />
            <path d="M88.5 63.5H91.5V60.5H88.5V63.5Z"  />
            <path d="M92.5 63.5H95.5V60.5H92.5V63.5Z"  />
            <path d="M0.5 59.5H3.5V56.5H0.5V59.5Z"  />
            <path d="M4.5 59.5H7.5V56.5H4.5V59.5Z"  />
            <path d="M8.5 59.5H11.5V56.5H8.5V59.5Z"  />
            <path d="M12.5 59.5H15.5V56.5H12.5V59.5Z"  />
            <path d="M16.5 59.5H19.5V56.5H16.5V59.5Z"  />
            <path d="M20.5 59.5H23.5V56.5H20.5V59.5Z"  />
            <path d="M24.5 59.5H27.5V56.5H24.5V59.5Z"  />
            <path d="M28.5 59.5H31.5V56.5H28.5V59.5Z"  />
            <path d="M32.5 59.5H35.5V56.5H32.5V59.5Z"  />
            <path d="M36.5 59.5H39.5V56.5H36.5V59.5Z"  />
            <path d="M40.5 59.5H43.5V56.5H40.5V59.5Z"  />
            <path d="M44.5 59.5H47.5V56.5H44.5V59.5Z"  />
            <path d="M48.5 59.5H51.5V56.5H48.5V59.5Z"  />
            <path d="M52.5 59.5H55.5V56.5H52.5V59.5Z"  />
            <path d="M56.5 59.5H59.5V56.5H56.5V59.5Z"  />
            <path d="M60.5 59.5H63.5V56.5H60.5V59.5Z"  />
            <path d="M64.5 59.5H67.5V56.5H64.5V59.5Z"  />
            <path d="M68.5 59.5H71.5V56.5H68.5V59.5Z"  />
            <path d="M72.5 59.5H75.5V56.5H72.5V59.5Z"  />
            <path d="M76.5 59.5H79.5V56.5H76.5V59.5Z"  />
            <path d="M80.5 59.5H83.5V56.5H80.5V59.5Z"  />
            <path d="M84.5 59.5H87.5V56.5H84.5V59.5Z"  />
            <path d="M88.5 59.5H91.5V56.5H88.5V59.5Z"  />
            <path d="M92.5 59.5H95.5V56.5H92.5V59.5Z"  />
            <path d="M0.5 55.5H3.5V52.5H0.5V55.5Z"  />
            <path d="M4.5 55.5H7.5V52.5H4.5V55.5Z"  />
            <path d="M8.5 55.5H11.5V52.5H8.5V55.5Z"  />
            <path d="M12.5 55.5H15.5V52.5H12.5V55.5Z"  />
            <path d="M16.5 55.5H19.5V52.5H16.5V55.5Z"  />
            <path d="M20.5 55.5H23.5V52.5H20.5V55.5Z"  />
            <path d="M24.5 55.5H27.5V52.5H24.5V55.5Z"  />
            <path d="M28.5 55.5H31.5V52.5H28.5V55.5Z"  />
            <path d="M32.5 55.5H35.5V52.5H32.5V55.5Z"  />
            <path d="M36.5 55.5H39.5V52.5H36.5V55.5Z"  />
            <path d="M40.5 55.5H43.5V52.5H40.5V55.5Z"  />
            <path d="M44.5 55.5H47.5V52.5H44.5V55.5Z"  />
            <path d="M48.5 55.5H51.5V52.5H48.5V55.5Z"  />
            <path d="M52.5 55.5H55.5V52.5H52.5V55.5Z"  />
            <path d="M56.5 55.5H59.5V52.5H56.5V55.5Z"  />
            <path d="M60.5 55.5H63.5V52.5H60.5V55.5Z"  />
            <path d="M64.5 55.5H67.5V52.5H64.5V55.5Z"  />
            <path d="M68.5 55.5H71.5V52.5H68.5V55.5Z"  />
            <path d="M72.5 55.5H75.5V52.5H72.5V55.5Z"  />
            <path d="M76.5 55.5H79.5V52.5H76.5V55.5Z"  />
            <path d="M80.5 55.5H83.5V52.5H80.5V55.5Z"  />
            <path d="M84.5 55.5H87.5V52.5H84.5V55.5Z"  />
            <path d="M88.5 55.5H91.5V52.5H88.5V55.5Z"  />
            <path d="M92.5 55.5H95.5V52.5H92.5V55.5Z"  />
            <path d="M0.5 51.5H3.5V48.5H0.5V51.5Z"  />
            <path d="M4.5 51.5H7.5V48.5H4.5V51.5Z"  />
            <path d="M8.5 51.5H11.5V48.5H8.5V51.5Z"  />
            <path d="M12.5 51.5H15.5V48.5H12.5V51.5Z"  />
            <path d="M16.5 51.5H19.5V48.5H16.5V51.5Z"  />
            <path d="M20.5 51.5H23.5V48.5H20.5V51.5Z"  />
            <path d="M24.5 51.5H27.5V48.5H24.5V51.5Z"  />
            <path d="M28.5 51.5H31.5V48.5H28.5V51.5Z"  />
            <path d="M32.5 51.5H35.5V48.5H32.5V51.5Z"  />
            <path d="M36.5 51.5H39.5V48.5H36.5V51.5Z"  />
            <path d="M40.5 51.5H43.5V48.5H40.5V51.5Z"  />
            <path d="M44.5 51.5H47.5V48.5H44.5V51.5Z"  />
            <path d="M48.5 51.5H51.5V48.5H48.5V51.5Z"  />
            <path d="M52.5 51.5H55.5V48.5H52.5V51.5Z"  />
            <path d="M56.5 51.5H59.5V48.5H56.5V51.5Z"  />
            <path d="M60.5 51.5H63.5V48.5H60.5V51.5Z"  />
            <path d="M64.5 51.5H67.5V48.5H64.5V51.5Z"  />
            <path d="M68.5 51.5H71.5V48.5H68.5V51.5Z"  />
            <path d="M72.5 51.5H75.5V48.5H72.5V51.5Z"  />
            <path d="M76.5 51.5H79.5V48.5H76.5V51.5Z"  />
            <path d="M80.5 51.5H83.5V48.5H80.5V51.5Z"  />
            <path d="M84.5 51.5H87.5V48.5H84.5V51.5Z"  />
            <path d="M88.5 51.5H91.5V48.5H88.5V51.5Z"  />
            <path d="M92.5 51.5H95.5V48.5H92.5V51.5Z"  />
            <path d="M0.5 47.5H3.5V44.5H0.5V47.5Z"  />
            <path d="M4.5 47.5H7.5V44.5H4.5V47.5Z"  />
            <path d="M8.5 47.5H11.5V44.5H8.5V47.5Z"  />
            <path d="M12.5 47.5H15.5V44.5H12.5V47.5Z"  />
            <path d="M16.5 47.5H19.5V44.5H16.5V47.5Z"  />
            <path d="M20.5 47.5H23.5V44.5H20.5V47.5Z"  />
            <path d="M24.5 47.5H27.5V44.5H24.5V47.5Z"  />
            <path d="M28.5 47.5H31.5V44.5H28.5V47.5Z"  />
            <path d="M32.5 47.5H35.5V44.5H32.5V47.5Z"  />
            <path d="M36.5 47.5H39.5V44.5H36.5V47.5Z"  />
            <path d="M40.5 47.5H43.5V44.5H40.5V47.5Z"  />
            <path d="M44.5 47.5H47.5V44.5H44.5V47.5Z"  />
            <path d="M48.5 47.5H51.5V44.5H48.5V47.5Z"  />
            <path d="M52.5 47.5H55.5V44.5H52.5V47.5Z"  />
            <path d="M56.5 47.5H59.5V44.5H56.5V47.5Z"  />
            <path d="M60.5 47.5H63.5V44.5H60.5V47.5Z"  />
            <path d="M64.5 47.5H67.5V44.5H64.5V47.5Z"  />
            <path d="M68.5 47.5H71.5V44.5H68.5V47.5Z"  />
            <path d="M72.5 47.5H75.5V44.5H72.5V47.5Z"  />
            <path d="M76.5 47.5H79.5V44.5H76.5V47.5Z"  />
            <path d="M80.5 47.5H83.5V44.5H80.5V47.5Z"  />
            <path d="M84.5 47.5H87.5V44.5H84.5V47.5Z"  />
            <path d="M88.5 47.5H91.5V44.5H88.5V47.5Z"  />
            <path d="M92.5 47.5H95.5V44.5H92.5V47.5Z"  />
            <path d="M0.5 43.5H3.5V40.5H0.5V43.5Z"  />
            <path d="M4.5 43.5H7.5V40.5H4.5V43.5Z"  />
            <path d="M8.5 43.5H11.5V40.5H8.5V43.5Z"  />
            <path d="M12.5 43.5H15.5V40.5H12.5V43.5Z"  />
            <path d="M16.5 43.5H19.5V40.5H16.5V43.5Z"  />
            <path d="M20.5 43.5H23.5V40.5H20.5V43.5Z"  />
            <path d="M24.5 43.5H27.5V40.5H24.5V43.5Z"  />
            <path d="M28.5 43.5H31.5V40.5H28.5V43.5Z"  />
            <path d="M32.5 43.5H35.5V40.5H32.5V43.5Z"  />
            <path d="M36.5 43.5H39.5V40.5H36.5V43.5Z"  />
            <path d="M40.5 43.5H43.5V40.5H40.5V43.5Z"  />
            <path d="M44.5 43.5H47.5V40.5H44.5V43.5Z"  />
            <path d="M48.5 43.5H51.5V40.5H48.5V43.5Z"  />
            <path d="M52.5 43.5H55.5V40.5H52.5V43.5Z"  />
            <path d="M56.5 43.5H59.5V40.5H56.5V43.5Z"  />
            <path d="M60.5 43.5H63.5V40.5H60.5V43.5Z"  />
            <path d="M64.5 43.5H67.5V40.5H64.5V43.5Z"  />
            <path d="M68.5 43.5H71.5V40.5H68.5V43.5Z"  />
            <path d="M72.5 43.5H75.5V40.5H72.5V43.5Z"  />
            <path d="M76.5 43.5H79.5V40.5H76.5V43.5Z"  />
            <path d="M80.5 43.5H83.5V40.5H80.5V43.5Z"  />
            <path d="M84.5 43.5H87.5V40.5H84.5V43.5Z"  />
            <path d="M88.5 43.5H91.5V40.5H88.5V43.5Z"  />
            <path d="M92.5 43.5H95.5V40.5H92.5V43.5Z"  />
            <path d="M0.5 39.5H3.5V36.5H0.5V39.5Z"  />
            <path d="M4.5 39.5H7.5V36.5H4.5V39.5Z"  />
            <path d="M8.5 39.5H11.5V36.5H8.5V39.5Z"  />
            <path d="M12.5 39.5H15.5V36.5H12.5V39.5Z"  />
            <path d="M16.5 39.5H19.5V36.5H16.5V39.5Z"  />
            <path d="M20.5 39.5H23.5V36.5H20.5V39.5Z"  />
            <path d="M24.5 39.5H27.5V36.5H24.5V39.5Z"  />
            <path d="M28.5 39.5H31.5V36.5H28.5V39.5Z"  />
            <path d="M32.5 39.5H35.5V36.5H32.5V39.5Z"  />
            <path d="M36.5 39.5H39.5V36.5H36.5V39.5Z"  />
            <path d="M40.5 39.5H43.5V36.5H40.5V39.5Z"  />
            <path d="M44.5 39.5H47.5V36.5H44.5V39.5Z"  />
            <path d="M48.5 39.5H51.5V36.5H48.5V39.5Z"  />
            <path d="M52.5 39.5H55.5V36.5H52.5V39.5Z"  />
            <path d="M56.5 39.5H59.5V36.5H56.5V39.5Z"  />
            <path d="M60.5 39.5H63.5V36.5H60.5V39.5Z"  />
            <path d="M64.5 39.5H67.5V36.5H64.5V39.5Z"  />
            <path d="M68.5 39.5H71.5V36.5H68.5V39.5Z"  />
            <path d="M72.5 39.5H75.5V36.5H72.5V39.5Z"  />
            <path d="M76.5 39.5H79.5V36.5H76.5V39.5Z"  />
            <path d="M80.5 39.5H83.5V36.5H80.5V39.5Z"  />
            <path d="M84.5 39.5H87.5V36.5H84.5V39.5Z"  />
            <path d="M88.5 39.5H91.5V36.5H88.5V39.5Z"  />
            <path d="M92.5 39.5H95.5V36.5H92.5V39.5Z"  />
            <path d="M0.5 35.5H3.5V32.5H0.5V35.5Z"  />
            <path d="M4.5 35.5H7.5V32.5H4.5V35.5Z"  />
            <path d="M8.5 35.5H11.5V32.5H8.5V35.5Z"  />
            <path d="M12.5 35.5H15.5V32.5H12.5V35.5Z"  />
            <path d="M16.5 35.5H19.5V32.5H16.5V35.5Z"  />
            <path d="M20.5 35.5H23.5V32.5H20.5V35.5Z"  />
            <path d="M24.5 35.5H27.5V32.5H24.5V35.5Z"  />
            <path d="M28.5 35.5H31.5V32.5H28.5V35.5Z"  />
            <path d="M32.5 35.5H35.5V32.5H32.5V35.5Z"  />
            <path d="M36.5 35.5H39.5V32.5H36.5V35.5Z"  />
            <path d="M40.5 35.5H43.5V32.5H40.5V35.5Z"  />
            <path d="M44.5 35.5H47.5V32.5H44.5V35.5Z"  />
            <path d="M48.5 35.5H51.5V32.5H48.5V35.5Z"  />
            <path d="M52.5 35.5H55.5V32.5H52.5V35.5Z"  />
            <path d="M56.5 35.5H59.5V32.5H56.5V35.5Z"  />
            <path d="M60.5 35.5H63.5V32.5H60.5V35.5Z"  />
            <path d="M64.5 35.5H67.5V32.5H64.5V35.5Z"  />
            <path d="M68.5 35.5H71.5V32.5H68.5V35.5Z"  />
            <path d="M72.5 35.5H75.5V32.5H72.5V35.5Z"  />
            <path d="M76.5 35.5H79.5V32.5H76.5V35.5Z"  />
            <path d="M80.5 35.5H83.5V32.5H80.5V35.5Z"  />
            <path d="M84.5 35.5H87.5V32.5H84.5V35.5Z"  />
            <path d="M88.5 35.5H91.5V32.5H88.5V35.5Z"  />
            <path d="M92.5 35.5H95.5V32.5H92.5V35.5Z"  />
            <path d="M4.5 31.5H7.5V28.5H4.5V31.5Z"  />
            <path d="M8.5 31.5H11.5V28.5H8.5V31.5Z"  />
            <path d="M12.5 31.5H15.5V28.5H12.5V31.5Z"  />
            <path d="M16.5 31.5H19.5V28.5H16.5V31.5Z"  />
            <path d="M20.5 31.5H23.5V28.5H20.5V31.5Z"  />
            <path d="M24.5 31.5H27.5V28.5H24.5V31.5Z"  />
            <path d="M28.5 31.5H31.5V28.5H28.5V31.5Z"  />
            <path d="M32.5 31.5H35.5V28.5H32.5V31.5Z"  />
            <path d="M36.5 31.5H39.5V28.5H36.5V31.5Z"  />
            <path d="M40.5 31.5H43.5V28.5H40.5V31.5Z"  />
            <path d="M44.5 31.5H47.5V28.5H44.5V31.5Z"  />
            <path d="M48.5 31.5H51.5V28.5H48.5V31.5Z"  />
            <path d="M52.5 31.5H55.5V28.5H52.5V31.5Z"  />
            <path d="M56.5 31.5H59.5V28.5H56.5V31.5Z"  />
            <path d="M60.5 31.5H63.5V28.5H60.5V31.5Z"  />
            <path d="M64.5 31.5H67.5V28.5H64.5V31.5Z"  />
            <path d="M68.5 31.5H71.5V28.5H68.5V31.5Z"  />
            <path d="M72.5 31.5H75.5V28.5H72.5V31.5Z"  />
            <path d="M76.5 31.5H79.5V28.5H76.5V31.5Z"  />
            <path d="M80.5 31.5H83.5V28.5H80.5V31.5Z"  />
            <path d="M84.5 31.5H87.5V28.5H84.5V31.5Z"  />
            <path d="M88.5 31.5H91.5V28.5H88.5V31.5Z"  />
            <path d="M4.5 27.5H7.5V24.5H4.5V27.5Z"  />
            <path d="M8.5 27.5H11.5V24.5H8.5V27.5Z"  />
            <path d="M12.5 27.5H15.5V24.5H12.5V27.5Z"  />
            <path d="M16.5 27.5H19.5V24.5H16.5V27.5Z"  />
            <path d="M20.5 27.5H23.5V24.5H20.5V27.5Z"  />
            <path d="M24.5 27.5H27.5V24.5H24.5V27.5Z"  />
            <path d="M28.5 27.5H31.5V24.5H28.5V27.5Z"  />
            <path d="M32.5 27.5H35.5V24.5H32.5V27.5Z"  />
            <path d="M36.5 27.5H39.5V24.5H36.5V27.5Z"  />
            <path d="M40.5 27.5H43.5V24.5H40.5V27.5Z"  />
            <path d="M44.5 27.5H47.5V24.5H44.5V27.5Z"  />
            <path d="M48.5 27.5H51.5V24.5H48.5V27.5Z"  />
            <path d="M52.5 27.5H55.5V24.5H52.5V27.5Z"  />
            <path d="M56.5 27.5H59.5V24.5H56.5V27.5Z"  />
            <path d="M60.5 27.5H63.5V24.5H60.5V27.5Z"  />
            <path d="M64.5 27.5H67.5V24.5H64.5V27.5Z"  />
            <path d="M68.5 27.5H71.5V24.5H68.5V27.5Z"  />
            <path d="M72.5 27.5H75.5V24.5H72.5V27.5Z"  />
            <path d="M76.5 27.5H79.5V24.5H76.5V27.5Z"  />
            <path d="M80.5 27.5H83.5V24.5H80.5V27.5Z"  />
            <path d="M84.5 27.5H87.5V24.5H84.5V27.5Z"  />
            <path d="M88.5 27.5H91.5V24.5H88.5V27.5Z"  />
            <path d="M8.5 23.5H11.5V20.5H8.5V23.5Z"  />
            <path d="M12.5 23.5H15.5V20.5H12.5V23.5Z"  />
            <path d="M16.5 23.5H19.5V20.5H16.5V23.5Z"  />
            <path d="M20.5 23.5H23.5V20.5H20.5V23.5Z"  />
            <path d="M24.5 23.5H27.5V20.5H24.5V23.5Z"  />
            <path d="M28.5 23.5H31.5V20.5H28.5V23.5Z"  />
            <path d="M32.5 23.5H35.5V20.5H32.5V23.5Z"  />
            <path d="M36.5 23.5H39.5V20.5H36.5V23.5Z"  />
            <path d="M40.5 23.5H43.5V20.5H40.5V23.5Z"  />
            <path d="M44.5 23.5H47.5V20.5H44.5V23.5Z"  />
            <path d="M48.5 23.5H51.5V20.5H48.5V23.5Z"  />
            <path d="M52.5 23.5H55.5V20.5H52.5V23.5Z"  />
            <path d="M56.5 23.5H59.5V20.5H56.5V23.5Z"  />
            <path d="M60.5 23.5H63.5V20.5H60.5V23.5Z"  />
            <path d="M64.5 23.5H67.5V20.5H64.5V23.5Z"  />
            <path d="M68.5 23.5H71.5V20.5H68.5V23.5Z"  />
            <path d="M72.5 23.5H75.5V20.5H72.5V23.5Z"  />
            <path d="M76.5 23.5H79.5V20.5H76.5V23.5Z"  />
            <path d="M80.5 23.5H83.5V20.5H80.5V23.5Z"  />
            <path d="M84.5 23.5H87.5V20.5H84.5V23.5Z"  />
            <path d="M8.5 19.5H11.5V16.5H8.5V19.5Z"  />
            <path d="M12.5 19.5H15.5V16.5H12.5V19.5Z"  />
            <path d="M16.5 19.5H19.5V16.5H16.5V19.5Z"  />
            <path d="M20.5 19.5H23.5V16.5H20.5V19.5Z"  />
            <path d="M24.5 19.5H27.5V16.5H24.5V19.5Z"  />
            <path d="M28.5 19.5H31.5V16.5H28.5V19.5Z"  />
            <path d="M32.5 19.5H35.5V16.5H32.5V19.5Z"  />
            <path d="M36.5 19.5H39.5V16.5H36.5V19.5Z"  />
            <path d="M40.5 19.5H43.5V16.5H40.5V19.5Z"  />
            <path d="M44.5 19.5H47.5V16.5H44.5V19.5Z"  />
            <path d="M48.5 19.5H51.5V16.5H48.5V19.5Z"  />
            <path d="M52.5 19.5H55.5V16.5H52.5V19.5Z"  />
            <path d="M56.5 19.5H59.5V16.5H56.5V19.5Z"  />
            <path d="M60.5 19.5H63.5V16.5H60.5V19.5Z"  />
            <path d="M64.5 19.5H67.5V16.5H64.5V19.5Z"  />
            <path d="M68.5 19.5H71.5V16.5H68.5V19.5Z"  />
            <path d="M72.5 19.5H75.5V16.5H72.5V19.5Z"  />
            <path d="M76.5 19.5H79.5V16.5H76.5V19.5Z"  />
            <path d="M80.5 19.5H83.5V16.5H80.5V19.5Z"  />
            <path d="M84.5 19.5H87.5V16.5H84.5V19.5Z"  />
            <path d="M12.5 15.5H15.5V12.5H12.5V15.5Z"  />
            <path d="M16.5 15.5H19.5V12.5H16.5V15.5Z"  />
            <path d="M20.5 15.5H23.5V12.5H20.5V15.5Z"  />
            <path d="M24.5 15.5H27.5V12.5H24.5V15.5Z"  />
            <path d="M28.5 15.5H31.5V12.5H28.5V15.5Z"  />
            <path d="M32.5 15.5H35.5V12.5H32.5V15.5Z"  />
            <path d="M36.5 15.5H39.5V12.5H36.5V15.5Z"  />
            <path d="M40.5 15.5H43.5V12.5H40.5V15.5Z"  />
            <path d="M44.5 15.5H47.5V12.5H44.5V15.5Z"  />
            <path d="M48.5 15.5H51.5V12.5H48.5V15.5Z"  />
            <path d="M52.5 15.5H55.5V12.5H52.5V15.5Z"  />
            <path d="M56.5 15.5H59.5V12.5H56.5V15.5Z"  />
            <path d="M60.5 15.5H63.5V12.5H60.5V15.5Z"  />
            <path d="M64.5 15.5H67.5V12.5H64.5V15.5Z"  />
            <path d="M68.5 15.5H71.5V12.5H68.5V15.5Z"  />
            <path d="M72.5 15.5H75.5V12.5H72.5V15.5Z"  />
            <path d="M76.5 15.5H79.5V12.5H76.5V15.5Z"  />
            <path d="M80.5 15.5H83.5V12.5H80.5V15.5Z"  />
            <path d="M16.5 11.5H19.5V8.5H16.5V11.5Z"  />
            <path d="M20.5 11.5H23.5V8.5H20.5V11.5Z"  />
            <path d="M24.5 11.5H27.5V8.5H24.5V11.5Z"  />
            <path d="M28.5 11.5H31.5V8.5H28.5V11.5Z"  />
            <path d="M32.5 11.5H35.5V8.5H32.5V11.5Z"  />
            <path d="M36.5 11.5H39.5V8.5H36.5V11.5Z"  />
            <path d="M40.5 11.5H43.5V8.5H40.5V11.5Z"  />
            <path d="M44.5 11.5H47.5V8.5H44.5V11.5Z"  />
            <path d="M48.5 11.5H51.5V8.5H48.5V11.5Z"  />
            <path d="M52.5 11.5H55.5V8.5H52.5V11.5Z"  />
            <path d="M56.5 11.5H59.5V8.5H56.5V11.5Z"  />
            <path d="M60.5 11.5H63.5V8.5H60.5V11.5Z"  />
            <path d="M64.5 11.5H67.5V8.5H64.5V11.5Z"  />
            <path d="M68.5 11.5H71.5V8.5H68.5V11.5Z"  />
            <path d="M72.5 11.5H75.5V8.5H72.5V11.5Z"  />
            <path d="M76.5 11.5H79.5V8.5H76.5V11.5Z"  />
            <path d="M24.5 7.5H27.5V4.5H24.5V7.5Z"  />
            <path d="M28.5 7.5H31.5V4.5H28.5V7.5Z"  />
            <path d="M32.5 7.5H35.5V4.5H32.5V7.5Z"  />
            <path d="M36.5 7.5H39.5V4.5H36.5V7.5Z"  />
            <path d="M40.5 7.5H43.5V4.5H40.5V7.5Z"  />
            <path d="M44.5 7.5H47.5V4.5H44.5V7.5Z"  />
            <path d="M48.5 7.5H51.5V4.5H48.5V7.5Z"  />
            <path d="M52.5 7.5H55.5V4.5H52.5V7.5Z"  />
            <path d="M56.5 7.5H59.5V4.5H56.5V7.5Z"  />
            <path d="M60.5 7.5H63.5V4.5H60.5V7.5Z"  />
            <path d="M64.5 7.5H67.5V4.5H64.5V7.5Z"  />
            <path d="M68.5 7.5H71.5V4.5H68.5V7.5Z"  />
            <path d="M32.5 3.5H35.5V0.5H32.5V3.5Z"  />
            <path d="M36.5 3.5H39.5V0.5H36.5V3.5Z"  />
            <path d="M40.5 3.5H43.5V0.5H40.5V3.5Z"  />
            <path d="M44.5 3.5H47.5V0.5H44.5V3.5Z"  />
            <path d="M48.5 3.5H51.5V0.5H48.5V3.5Z"  />
            <path d="M52.5 3.5H55.5V0.5H52.5V3.5Z"  />
            <path d="M56.5 3.5H59.5V0.5H56.5V3.5Z"  />
            <path d="M60.5 3.5H63.5V0.5H60.5V3.5Z"  />
        </g>
        <g id="punk_fill" transform="scale(0.25)">
            <rect x="24.5" y="55.5" width="4" height="40" fill="black" />
            <rect x="20.5" y="47.5" width="4" height="12" fill="black" />
            <rect x="24.5" y="27.5" width="4" height="20" fill="black" />
            <rect x="28.5" y="23.5" width="4" height="4" fill="black" />
            <rect x="32.5" y="19.5" width="28" height="4" fill="black" />
            <rect x="60.5" y="23.5" width="4" height="4" fill="black" />
            <rect x="64.5" y="27.5" width="4" height="52" fill="black" />
            <rect x="60.5" y="79.5" width="4" height="4" fill="black" />
            <rect x="40.5" y="83.5" width="20" height="4" fill="black" />
            <rect x="40.5" y="87.5" width="4" height="8" fill="black" />
            <rect x="44.5" y="71.5" width="12" height="4" fill="black" />
            <rect x="48.5" y="59.5" width="8" height="4" fill="black" />
            <rect x="56.5" y="47.5" width="4" height="4" fill="black" />
            <rect x="36.5" y="47.5" width="4" height="4" fill="black" />
            <rect x="40.5" y="44.5" width="3" height="3" fill="black" />
            <rect x="36.5" y="44.5" width="3" height="3" fill="black" />
            <rect x="56.5" y="48.5" width="3" height="3" fill="black" />
            <rect x="56.5" y="44.5" width="3" height="3" fill="black" />
            <rect x="60.5" y="44.5" width="3" height="3" fill="black" />
            <rect x="36.5" y="48.5" width="3" height="3" fill="black" />
        </g>
    </defs>

"""
punk_string += board_string
end_string = """
</svg>
"""
piece_1 = f"""
    <use href="#punk_main" fill=[color] transform="translate(8 8)" />
    <use href="#punk_fill" transform="translate(8 8)"/>
"""

piece_2 = f"""
    <use href="#punk_main" fill=[color] transform="translate(36 8)" />
    <use href="#punk_fill" transform="translate(36 8)"/>
"""

piece_3 = f"""
    <use href="#punk_main" fill=[color] transform="translate(64 8)" />
    <use href="#punk_fill" transform="translate(64 8)"/>
"""
piece_4 = f"""
    <use href="#punk_main" fill=[color] transform="translate(8 36)" />
    <use href="#punk_fill" transform="translate(8 36)"/>
"""

piece_5 = f"""
    <use href="#punk_main" fill=[color] transform="translate(36 36)" />
    <use href="#punk_fill" transform="translate(36 36) "/>
"""

piece_6 = f"""
    <use href="#punk_main" fill=[color] transform="translate(64 36)" />
    <use href="#punk_fill" transform="translate(64 36)"/>  
"""
piece_7 = f"""
      <use href="#punk_main" fill=[color] transform="translate(8 64)" />
    <use href="#punk_fill" transform="translate(8 64)"/>
"""
piece_8 = f"""
    <use href="#punk_main" fill=[color] transform="translate(36 64)" />
    <use href="#punk_fill" transform="translate(36 64)"/>
"""
piece_9 = f"""
    <use href="#punk_main" fill=[color] transform="translate(64 64)" />
    <use href="#punk_fill" transform="translate(64 64)"/>
"""

punk_pieces = [piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7, piece_8, piece_9]

def replace_color(string, new_color):
    return string.replace("[color]", new_color)

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def play_game():
    global punk_string
    board = [' '] * 9
    player1 = 'X'
    player2 = 'O'
    current_player = player1
    colors = {
        player1: random_color_1,
        player2: random_color_2
    }
    while True:


        # Player makes a move
        while True:
            move = random.randint(0, 8)
            if board[move] == ' ':
                piece_string = replace_color(punk_pieces[move], colors[current_player])
                punk_string += piece_string
                board[move] = current_player
                break


        # Check for a winner
        if check_win(board, current_player):

            return

        # Check for a tie
        if ' ' not in board:

            return

        # Switch to the other player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

if __name__ == "__main__":
    play_game()

    punk_string += (end_string)
    current_time = datetime.datetime.now().strftime("%H_%M_%S")
    file_name = f"{current_time}.svg"
    with open(file_name, 'w') as file:
        # Use the print function with the file parameter to write to the file
        print(punk_string, file=file)
    print(f"SVG written to {file_name}")
