<template>
  <div class="home">
    <b-container class='mt-3 mb-4'>
      <h3 class="d-flex justify-content-center">Регистрирани участници:</h3>
    </b-container>
  
    <Participants />
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
