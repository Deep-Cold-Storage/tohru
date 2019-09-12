import Vue from "vue";
import App from "./App.vue";
import VueScrollTo from 'vue-scrollto';
import Axios from 'axios'

Vue.prototype.$http = Axios;
Vue.config.productionTip = false;

Vue.use(VueScrollTo);

new Vue({
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
