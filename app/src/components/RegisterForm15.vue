<template>
  <div>
    <b-card
      overlay
      img-src="../assets/pictures/13banner.jpg"
      img-alt="Card Image"
      text-variant="white"
      class='text-right'
      title=""
      sub-title=""
    >
      <div id="card-div">

      <h1 id='card-txt'>13км СКАЙ</h1>
      <h2 id='card-txt-small'>1700м положителна денивелация</h2>
      </div>
    </b-card>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show"  class="p-3 reg-form">
      <b-row>
        <b-col>
          <b-form-group id="input-group-1" label="Електронна поща:" label-for="input-1">
            <b-form-input id="input-1" v-model="form.email" type="email" required placeholder="Въведи поща"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group id="input-group-1" label="Телефонен номер:" label-for="input-1">
            <b-form-input v-model="form.phone_number" type="text" maxlength="15" required placeholder="Въведи телефон за връзка"></b-form-input>
          </b-form-group>
        </b-col>
      </b-row>
      <b-form-group id="input-group-2" label="Имена:" label-for="input-2">
        <b-row>
          <b-col sm>
            <b-form-input v-model="form.firstname" required placeholder="Първо име"></b-form-input>
          </b-col>
          <b-col sm>
            <b-form-input v-model="form.secondname" required placeholder="Бащино име"></b-form-input>
          </b-col>
          <b-col sm>
            <b-form-input v-model="form.lastname" required placeholder="Фамилия"></b-form-input>
          </b-col>        
        </b-row>
      </b-form-group>

      <b-row>
          <b-col sm>
            <b-form-group id="input-group-3" label="Пол:" label-for="input-3">
              <b-form-select id="input-3" v-model="form.gender" :options="genders" required></b-form-select>
            </b-form-group>
          </b-col>
        
         
          <b-col sm>
            <b-form-group label="Допълнителни легла:" description="Допълнителни легла за спане в хижа Плевен">
              <b-form-input type="number" min="0"  max="7" placeholder="Брой допълнителни легла" v-model="form.extraBeds"></b-form-input>
            </b-form-group>
          </b-col>
        
      </b-row>

      <b-row class='text-center'>
        <b-col>
          <b-button type="submit" variant="primary" class="mr-1">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-col>
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
        distance: "sky",
        email: "",
        phone_number: "",
        firstname: "",
        secondname: "",
        lastname: "",
        gender: null,
        age: 20,
        extraBeds: 0,
      },
      genders: [{ text: "Select One", value: null }, "Male", "Female"],
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.submitForm();
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.firstname = "";
      this.form.secondname = "";
      this.form.lastname = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    submitForm() {
      axios
        .post(this.api_uri['athlete'], {
          first_name: this.form.firstname,
          second_name: this.form.secondname,
          last_name: this.form.lastname,
          email: this.form.email,
          phone_number: this.form.phone_number,
          gender: this.form.gender,
          age: this.form.age,
          bonus_beds: this.form.extraBeds,
          distance: this.form.distance,
          link: "",
        })
        .then(
          (response)=> {
            console.log(response)
            this.$router.push("Success")
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  },
};
</script>

<style scoped>
.reg-form {
  border: 3px solid lightseagreen;
}

#card-txt-small {
  color: rgb(68, 214, 233);
  font-family: 'SPArielBG';
  margin-right: 5%;
  font-size: 2vw;
}

#card-txt{
  font-family: 'SPArielBG';
  font-weight: bold;
  font-style: italic;
  color: rgb(135, 248, 248);
  font-size: 7vw;
  margin-right: 5%;
}
</style>
