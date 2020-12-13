<template>
  <div class="m-3">
    <b-container>
      <div class="frame">
        <b-table
          striped
          hover
          :items="athletes"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
    </b-container>
  </div>
</template>
<script>
const axios = require("axios").default;

export default {
  name: "Participants",
  data() {
    return {
      testvam: null,
      fields: [
        {
          key: "first_name",
          sortable: false
        },
        {
          key: "last_name",
          sortable: false,
        },
        {
          key: "gender",
          sortable: true,
          // Variant applies to the whole column, including the header and footer
          variant: "",
        },
        {
          key: "distance",
          sortable: true,
        },
      ],
      athletes: [],
    };
  },
  methods: {
    getAthletes() {
      axios
        .get("http://127.0.0.1:5000/athlete")
        .then((response) => {
          console.log(response.data);
          this.athletes = response.data;
        })
        .catch(function(error) {
          console.log(error);
        })
        .then(function (){
            // always executed
        });
    },
    rowClass(item, type) {
      if (!item || type !== "row") return;
      if (item.Ranking !== "DNF") return "table-info";
      if (item.Ranking === "DNF") return "table-danger";
    },
  },
  mounted: function() {
    this.getAthletes()
    console.log("mounted");
  },
};
</script>

<style scoped>
.frame {
  border: 5px solid rgb(34, 60, 87);
}
</style>