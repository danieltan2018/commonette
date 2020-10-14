import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import Axios from "axios";

Vue.config.productionTip = false
Vue.prototype.$http = Axios;
Vue.prototype.$http.defaults.baseURL = "https://commonapi.smusis.com";
Vue.prototype.$appName = 'Commonette'


new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
