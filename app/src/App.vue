<template>
  <div>
    <div id="mynavbar" class="mb-2">
      <Navbar />
    </div>
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
#mynavbar{
  box-shadow: 0 4px 6px 1px rgb(107, 107, 107);
}
</style>
