<template>
  <div class="home">
    <v-toolbar dark>
      <v-spacer></v-spacer>
      <router-link to="/">
        <v-btn text>
          Home
        </v-btn>
      </router-link>
      <router-link to="sign-up">
        <v-btn text>
          Register
        </v-btn>
      </router-link>
      <v-btn text>
        Athletes
      </v-btn>
      <router-link to="about" tag="button">
        <v-btn text>
          Race Info
        </v-btn></router-link
      >
      <v-spacer></v-spacer>
    </v-toolbar>
  </div>
</template>

<script>
export default {
  name: "NavBar",

  data: () => ({}),
};
</script>
