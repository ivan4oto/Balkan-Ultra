<template>
  <div>
    <div class='wrapper'>
      <div id="mynavbar" class="mb-2">
        <Navbar />
      </div>
      <div class='rw'>
      <router-view />
      </div>
    </div>
    <div class='bottom-bg'>
      <b-row align-h="center">
      <div class="sponsors">
        <Sponsors />
      </div>
      </b-row>
    </div>
    <div class='page-footer'>
      <Footer />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import Sponsors from "./components/Sponsors.vue";


export default {
  name: "App",
  components: {
    Navbar,
    Footer,
    Sponsors,
  },
};
</script>

<style>
#mynavbar{
  box-shadow: 0 4px 6px 1px rgb(107, 107, 107);
}
.wrapper {
  min-height: calc(100vh - 80px);
}
.page-footer {
  height: 60px;
}
.bottom-bg{
  height: 500px;
  width: 100%;
  background-image: url('./assets/pictures/bg-image.jpg');
  position: relative
}
.sponsors {
    position: absolute;
    bottom: 0;
}
</style>
