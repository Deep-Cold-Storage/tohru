import Vue from "vue";
import App from "./App.vue";
import VueScrollTo from "vue-scrollto";
import VueObserveVisibility from "vue-observe-visibility";
import Axios from "axios";

Vue.prototype.$http = Axios;
Vue.config.productionTip = false;

Vue.use(VueScrollTo);
Vue.use(VueObserveVisibility);

new Vue({
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
