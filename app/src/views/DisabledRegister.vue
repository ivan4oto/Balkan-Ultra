<template>
  <div class="home">
    <b-container>
    <b-jumbotron bg-variant="info" text-variant="white" border-variant="dark">
        <template #header>Затворена!</template>

        <template #lead>
        Регистрацията за тазгодишното издание на Балкан Ултра е прекратена.
        </template>

    </b-jumbotron>
    </b-container>
  </div>
</template>

<script>

export default {
  name: "DisabledRegister",
  components: {
  },
  data(){
    return {
    }
  }
};
</script>

<style scoped>
</style>