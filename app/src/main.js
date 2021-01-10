import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import router from "./router";
import { BootstrapVueIcons} from 'bootstrap-vue';

Vue.use(BootstrapVueIcons, {})


Vue.config.productionTip = false;

Vue.mixin({
  data: function() {
    return {
      get api_uri() {
        var paths = require("./uri_config.json");
        return paths
      }
    }
  },
  methods: {
    isMobile() {
      if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        return true
      } else {
        return false
      }
    }
  },
})

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
