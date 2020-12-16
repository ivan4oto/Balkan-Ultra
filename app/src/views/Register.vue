<template>
  <div class="home">
    <b-container class="p-3">
      <b-button-group class="d-flex justify-content-center myborder">
        <b-button variant="danger" @click="activateUltra = true" id='ultra'>80k ULTRA</b-button>
        <b-button variant="info" @click="activateUltra = false" id='sky'>13k SKY</b-button>
      </b-button-group>
      <div v-if="!activateUltra">
        <RegisterForm15 />
      </div>
      <div v-if="activateUltra">
        <RegisterForm80 />
      </div>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import RegisterForm80 from "@/components/RegisterForm80.vue";
import RegisterForm15 from "@/components/RegisterForm15.vue";

export default {
  name: "Register",
  components: {
    RegisterForm80,
    RegisterForm15
  },
  data(){
    return {
      activateUltra: true
    }
  }
};
</script>

<style scoped>
  #ultra {
    border: 2px solid darkred;
  }
  #sky {
    border: 2px solid darkcyan;
  }
</style>