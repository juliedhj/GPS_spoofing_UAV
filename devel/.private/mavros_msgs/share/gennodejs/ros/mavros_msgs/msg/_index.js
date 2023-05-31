
"use strict";

let MagnetometerReporter = require('./MagnetometerReporter.js');
let CommandCode = require('./CommandCode.js');
let LogData = require('./LogData.js');
let Tunnel = require('./Tunnel.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let ActuatorControl = require('./ActuatorControl.js');
let ESCInfo = require('./ESCInfo.js');
let MountControl = require('./MountControl.js');
let GPSRTK = require('./GPSRTK.js');
let ESCStatus = require('./ESCStatus.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let PositionTarget = require('./PositionTarget.js');
let RCIn = require('./RCIn.js');
let WaypointList = require('./WaypointList.js');
let VFR_HUD = require('./VFR_HUD.js');
let RTCM = require('./RTCM.js');
let DebugValue = require('./DebugValue.js');
let GPSINPUT = require('./GPSINPUT.js');
let RCOut = require('./RCOut.js');
let HilSensor = require('./HilSensor.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let LandingTarget = require('./LandingTarget.js');
let BatteryStatus = require('./BatteryStatus.js');
let Vibration = require('./Vibration.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let ParamValue = require('./ParamValue.js');
let State = require('./State.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let RTKBaseline = require('./RTKBaseline.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let Altitude = require('./Altitude.js');
let HilGPS = require('./HilGPS.js');
let StatusText = require('./StatusText.js');
let Param = require('./Param.js');
let ManualControl = require('./ManualControl.js');
let HomePosition = require('./HomePosition.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let LogEntry = require('./LogEntry.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let CellularStatus = require('./CellularStatus.js');
let Trajectory = require('./Trajectory.js');
let GPSRAW = require('./GPSRAW.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let VehicleInfo = require('./VehicleInfo.js');
let Thrust = require('./Thrust.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let HilControls = require('./HilControls.js');
let WaypointReached = require('./WaypointReached.js');
let Waypoint = require('./Waypoint.js');
let FileEntry = require('./FileEntry.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let TerrainReport = require('./TerrainReport.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let RadioStatus = require('./RadioStatus.js');
let Mavlink = require('./Mavlink.js');
let ExtendedState = require('./ExtendedState.js');

module.exports = {
  MagnetometerReporter: MagnetometerReporter,
  CommandCode: CommandCode,
  LogData: LogData,
  Tunnel: Tunnel,
  WheelOdomStamped: WheelOdomStamped,
  OnboardComputerStatus: OnboardComputerStatus,
  ActuatorControl: ActuatorControl,
  ESCInfo: ESCInfo,
  MountControl: MountControl,
  GPSRTK: GPSRTK,
  ESCStatus: ESCStatus,
  HilActuatorControls: HilActuatorControls,
  ESCTelemetryItem: ESCTelemetryItem,
  PositionTarget: PositionTarget,
  RCIn: RCIn,
  WaypointList: WaypointList,
  VFR_HUD: VFR_HUD,
  RTCM: RTCM,
  DebugValue: DebugValue,
  GPSINPUT: GPSINPUT,
  RCOut: RCOut,
  HilSensor: HilSensor,
  CameraImageCaptured: CameraImageCaptured,
  HilStateQuaternion: HilStateQuaternion,
  LandingTarget: LandingTarget,
  BatteryStatus: BatteryStatus,
  Vibration: Vibration,
  NavControllerOutput: NavControllerOutput,
  TimesyncStatus: TimesyncStatus,
  ParamValue: ParamValue,
  State: State,
  CamIMUStamp: CamIMUStamp,
  RTKBaseline: RTKBaseline,
  ESCTelemetry: ESCTelemetry,
  Altitude: Altitude,
  HilGPS: HilGPS,
  StatusText: StatusText,
  Param: Param,
  ManualControl: ManualControl,
  HomePosition: HomePosition,
  AttitudeTarget: AttitudeTarget,
  LogEntry: LogEntry,
  OverrideRCIn: OverrideRCIn,
  ESCStatusItem: ESCStatusItem,
  CompanionProcessStatus: CompanionProcessStatus,
  GlobalPositionTarget: GlobalPositionTarget,
  CellularStatus: CellularStatus,
  Trajectory: Trajectory,
  GPSRAW: GPSRAW,
  ADSBVehicle: ADSBVehicle,
  ESCInfoItem: ESCInfoItem,
  VehicleInfo: VehicleInfo,
  Thrust: Thrust,
  EstimatorStatus: EstimatorStatus,
  HilControls: HilControls,
  WaypointReached: WaypointReached,
  Waypoint: Waypoint,
  FileEntry: FileEntry,
  OpticalFlowRad: OpticalFlowRad,
  TerrainReport: TerrainReport,
  PlayTuneV2: PlayTuneV2,
  RadioStatus: RadioStatus,
  Mavlink: Mavlink,
  ExtendedState: ExtendedState,
};
