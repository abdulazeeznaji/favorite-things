import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import ApiService from "./common/api.service";

ApiService.init();
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
