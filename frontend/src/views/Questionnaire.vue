import { required } from  'vuelidate/lib/validators'

<template>
    <v-container fluid justify-center>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6>
					<h1>Let's get to know you!</h1>
				</v-flex>
			</v-layout>
			<v-form ref="form">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-text-field label="Name" v-model="name" :rules="inputNameRules"></v-text-field>
					</v-flex>
				</v-layout>
				<h2>Youtube</h2>
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Categories" v-model="youtubeCategory" :items="inputYoutube" :rules="inputCategoryRules"></v-autocomplete>
					</v-flex>
				</v-layout>
				<v-btn text class="success mx-0 mt-3" @click="submit">Let's Go</v-btn>
			</v-form>
    </v-container>
</template>

<script>
export default {
  data: () => {
		return {
			name: '',
			youtubeCategory: '',
			inputYoutube: ["hello","there"],
			inputNameRules:[
				v => v.length > 0 || 'Please enter your name'
			],
			inputCategoryRules:[
				v => v.length > 0 || 'Required'
			]
		}
	},
	methods: {
		submit(){
			if (this.$refs.form.validate()){
				console.log(this.name);
				console.log(this.youtubeCategory)
			}
		}
	}
};
</script>