<template>
  <div class="home">
    <b-container class='mt-4 d-none d-sm-block' >
      <HelloWorld />
    </b-container>
    <div class='d-block d-sm-none'>
      <HelloWorld />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
};
</script>
