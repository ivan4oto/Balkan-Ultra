<template>
  <div>
    <div>
      <h2 class="d-flex justify-content-center m-3">
        Регистрирай се за 80км Ultra
      </h2>
    </div>
    <b-form
      @submit="onSubmit"
      @reset="onReset"
      v-if="show"
      class="p-4 reg-form"
    >
      <b-form-group
        id="input-group-1"
        label="Електронна поща:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
          placeholder="Въведи поща"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Имена:" label-for="input-2">
        <b-form-input
          class="mb-2"
          id="input-2"
          v-model="form.firstname"
          required
          placeholder="Първо име"
        ></b-form-input>

        <b-form-input
          id="input-2"
          class="mb-2"
          v-model="form.secondname"
          required
          placeholder="Бащино име"
        ></b-form-input>

        <b-form-input
          id="input-2"
          class="mb-2"
          v-model="form.lastname"
          required
          placeholder="Фамилия"
        ></b-form-input>
      </b-form-group>

      <b-form-row align-h="start">
        <b-col cols="4">
          <b-form-group id="input-group-3" label="Пол:" label-for="input-3">
            <b-form-select
              id="input-3"
              v-model="form.gender"
              :options="genders"
              required
            ></b-form-select>
          </b-form-group>
        </b-col>

        <b-col cols="4">
          <b-form-group
            label="Допълнителни легла:"
            description="Допълнителни легла за спане в хижа Плевен"
          >
            <b-form-input type="number" placeholder="Брой допълнителни легла" v-model="form.extraBeds">
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-form-row>

      <b-row align-h="start">
        <b-col cols="8">
          <b-form-group
            label="Линк към резултати:"
            description="Моля поставете линк към резултати от две състезания надхвърлящи 4000м положителна денивелация всяко."
          >
            <b-form-input type="url" v-model="raceLink"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="2">
          <b-button
            @click="addLink"
            size="sm"
            variant="outline-primary"
            class="mb-1"
            >Добави линк</b-button
          >
          <b-button size="sm" variant="outline-danger" @click="removeLink"
            >Премахни линк</b-button
          >
        </b-col>
      </b-row>

      <b-list-group v-for="link in form.raceLinks" v-bind:key="link">
        <b-list-group-item>{{ link }}</b-list-group-item>
      </b-list-group>

      <b-row class="justify-content-md-center pt-5">
        <b-button
          type="submit"
          variant="primary"
          class="mr-1"
          @click="submitForm()"
          >Submit</b-button
        >
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-row>
    </b-form>

    <!-- <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card> -->
  </div>
</template>

<script>
const axios = require("axios").default;

export default {
  name: "RegisterForm",
  data() {
    return {
      activateUltra: true,
      raceLink: "",
      form: {
        distance: "ultra",
        email: "",
        firstname: "",
        secondname: "",
        lastname: "",
        gender: null,
        age: 20,
        extraBeds: 0,
        raceLinks: [],
      },
      genders: [{ text: "Select One", value: null }, "Male", "Female"],
      show: true,
    };
  },
  methods: {
    addLink() {
      if (this.form.raceLinks.length > 2) {
        alert("Стига толкос брат");
      } else {
        this.form.raceLinks.push(this.raceLink);
        this.raceLink = "";
      }
    },
    removeLink() {
      this.form.raceLinks.pop();
    },
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.firstname = "";
      this.form.secondname = "";
      this.form.lastname = "";
      this.raceLinks = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    submitForm() {
      axios
        .post("http://127.0.0.1:5000/athlete", {
          first_name: this.form.firstname,
          second_name: this.form.secondname,
          last_name: this.form.lastname,
          email: this.form.email,
          gender: this.form.gender,
          age: this.form.age,
          bonus_beds: this.form.extraBeds,
          link: this.form.raceLinks,
          distance: this.form.distance
        })
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.reg-form {
  border: 10px solid lightseagreen;
}

h2 {
  color: brown;
}
</style>
