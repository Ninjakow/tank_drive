import wpilib
from wpilib.drive import DifferentialDrive
from ctre import WPI_TalonSRX

class Robot(wpilib.IterativeRobot):

    def robotInit(self):
        '''Create motors and stuff here'''

        self.gamepad = wpilib.XboxController(0)

        # Left side
        self.drive_motor_a = WPI_TalonSRX(0)
        self.drive_motor_b = WPI_TalonSRX(1)
        self.left = wpilib.SpeedControllerGroup(self.drive_motor_a, self.drive_motor_b)
        self.left.setInverted(True)

        # Right side
        self.drive_motor_c = WPI_TalonSRX(2)
        self.drive_motor_d = WPI_TalonSRX(3)
        self.right = wpilib.SpeedControllerGroup(self.drive_motor_c, self.drive_motor_d)
        self.right.setInverted(True)

        self.drive_base = wpilib.drive.DifferentialDrive(self.left, self.right)

    def disabledInit(self):
        self.drive_base.stopMotor()

    def teleopPeriodic(self):
        '''Called on each iteration of the control loop'''
        throttle = self.gamepad.getY(wpilib.interfaces.GenericHID.Hand.kLeft)
        turn= self.gamepad.getX(wpilib.interfaces.GenericHID.Hand.kRight)

        self.drive_base.arcadeDrive(throttle, turn*-1)


if __name__ == '__main__':
    wpilib.run(Robot)
