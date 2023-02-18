class Config {
  constructor() {

  }
}

// API接口根url
// Config.baseUrl = 'http://192.168.43.39:8080';
Config.baseUrl = 'http://localhost:8080';
// 缓存有效期(毫秒)
Config.expired = 7200000;

Config.key = 'VSHBZ-44ZL4-GWPUX-XAEJ7-X25YE-C4BV6'; //在腾讯地图开放平台可以申请

// 地图导航Api
Config.mapApi = 'https://apis.map.qq.com/ws/direction/v1/';

// 导航智能语音
Config.navApi = 'https://api.ai.qq.com/path/to/api';

// 最长距离限制
Config.distanceMax = 21000;

export { Config };
