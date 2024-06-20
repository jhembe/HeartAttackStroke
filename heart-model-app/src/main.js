import { createApp } from 'vue'
import App from './App.vue'
import { BootstrapVueNext, } from 'bootstrap-vue-next'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'
// import 'animate.css'
// Vue.config.productionTip = false


createApp(App).use(BootstrapVueNext).mount('#app')
// app.use(BootstrapVueNext)
// app.mount('#app')
