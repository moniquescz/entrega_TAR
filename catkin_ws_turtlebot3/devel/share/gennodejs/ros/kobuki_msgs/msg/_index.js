
"use strict";

let CliffEvent = require('./CliffEvent.js');
let BumperEvent = require('./BumperEvent.js');
let ExternalPower = require('./ExternalPower.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let ButtonEvent = require('./ButtonEvent.js');
let Sound = require('./Sound.js');
let MotorPower = require('./MotorPower.js');
let ControllerInfo = require('./ControllerInfo.js');
let Led = require('./Led.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let VersionInfo = require('./VersionInfo.js');
let WheelDropEvent = require('./WheelDropEvent.js');
let DockInfraRed = require('./DockInfraRed.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let DigitalOutput = require('./DigitalOutput.js');
let KeyboardInput = require('./KeyboardInput.js');
let ScanAngle = require('./ScanAngle.js');
let SensorState = require('./SensorState.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingAction = require('./AutoDockingAction.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');

module.exports = {
  CliffEvent: CliffEvent,
  BumperEvent: BumperEvent,
  ExternalPower: ExternalPower,
  DigitalInputEvent: DigitalInputEvent,
  ButtonEvent: ButtonEvent,
  Sound: Sound,
  MotorPower: MotorPower,
  ControllerInfo: ControllerInfo,
  Led: Led,
  PowerSystemEvent: PowerSystemEvent,
  VersionInfo: VersionInfo,
  WheelDropEvent: WheelDropEvent,
  DockInfraRed: DockInfraRed,
  RobotStateEvent: RobotStateEvent,
  DigitalOutput: DigitalOutput,
  KeyboardInput: KeyboardInput,
  ScanAngle: ScanAngle,
  SensorState: SensorState,
  AutoDockingResult: AutoDockingResult,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingAction: AutoDockingAction,
  AutoDockingFeedback: AutoDockingFeedback,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
};
