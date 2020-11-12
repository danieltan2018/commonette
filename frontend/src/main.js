import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import Axios from "axios";
import AOS from 'aos';
import 'aos/dist/aos.css';
import Clipboard from "v-clipboard";

Vue.config.productionTip = false
Vue.prototype.$http = Axios;
Vue.prototype.$http.defaults.baseURL = "https://commonapi.smusis.com";
Vue.prototype.$bus = new Vue()
Vue.use(Clipboard);

new Vue({
  vuetify,
  router,
  created() {
    AOS.init()
  },
  render: h => h(App)
}).$mount('#app')
