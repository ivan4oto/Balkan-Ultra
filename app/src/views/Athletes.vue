<template>
  <div class="home">
    <b-container class='mt-4 d-none d-sm-block' >
      <h3 class="d-flex justify-content-center">Регистрирани участници:</h3>
      <Participants />
    </b-container>
    <div class='d-block d-sm-none'>
      <Participants />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Participants from "@/components/Participants.vue";

export default {
  name: "Athletes",
  components: {
    Participants,
  },
};
</script>
