<!-- <template>
  <div class="container mx-auto p-8 bg-gray-100 rounded-lg shadow-lg h-screen flex items-center">
    <h1 class="text-4xl font-bold text-center text-blue-700 mb-6">Patient Prediction Form</h1>
    <form @submit.prevent="getPrediction" class="prediction-form grid grid-cols-1 md:grid-cols-2 gap-4">
      Form Fields
      <div class="form-group" v-for="(field, index) in formFields" :key="index">
        <label :for="field.id" class="block text-sm font-medium text-gray-700">{{ field.label }}</label>
        <component :is="field.component" v-model.number="field.model" :type="field.type" :placeholder="field.placeholder" :id="field.id" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
          <option v-for="option in field.options" :value="option.value" :key="option.value">{{ option.text }}</option>
        </component>
      </div>
      <div class="col-span-1 md:col-span-2 flex justify-center">
        <button type="submit" class="submit-button w-full md:w-auto bg-blue-600 text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">Predict</button>
      </div>
    </form>

    Modal
    <transition name="fade">
      <div v-if="showModal" class="fixed inset-0 flex items-center justify-center z-50">
        <div class="modal-overlay absolute inset-0 bg-black opacity-50"></div>
        <div class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto">
          <div class="modal-content py-4 text-left px-6">
            <div class="flex justify-between items-center pb-3">
              <p class="text-2xl font-bold">Prediction Result</p>
              <div class="modal-close cursor-pointer z-50" @click="closeModal">
                <svg class="fill-current text-black" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                  <path d="M14.53 4.53a.75.75 0 00-1.06 0L9 8.94 4.53 4.47a.75.75 0 10-1.06 1.06L7.94 10l-4.47 4.47a.75.75 0 101.06 1.06L9 11.06l4.47 4.47a.75.75 0 001.06-1.06L10.06 10l4.47-4.47a.75.75 0 000-1.06z"/>
                </svg>
              </div>
            </div>

            <div class="mt-4">
              <p><strong>Prediction:</strong> {{ prediction }}</p>
              <div v-if="deviations && Object.keys(deviations).length > 0">
                <p><strong>Probable Causes:</strong></p>
                <ul>
                  <li v-for="(value, feature) in deviations" :key="feature">
                    {{ feature }}: {{ value }}
                  </li>
                </ul>
              </div>
            </div>

            <div class="flex justify-end pt-2">
              <button class="modal-close px-4 bg-indigo-500 p-3 rounded-lg text-white hover:bg-indigo-400" @click="closeModal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      age: null,
      sex: null,
      cp: null,
      trtbps: null,
      chol: null,
      fbs: null,
      restecg: null,
      thalachh: null,
      exng: null,
      oldpeak: null,
      slp: null,
      caa: null,
      thall: null,
      prediction: null,
      deviations: null,
      showModal: false,
      formFields: [
        { id: 'age', label: 'Age', component: 'input', type: 'number', placeholder: 'Enter age', model: 'age' },
        { id: 'sex', label: 'Gender', component: 'select', options: [{ value: 0, text: 'Male' }, { value: 1, text: 'Female' }], model: 'sex' },
        { id: 'cp', label: 'Chest Pain Type', component: 'select', options: [{ value: 0, text: 'Typical Angina' }, { value: 1, text: 'Atypical Angina' }, { value: 2, text: 'Non-Anginal Pain' }, { value: 3, text: 'Asymptomatic' }], model: 'cp' },
        { id: 'trtbps', label: 'Resting Blood Pressure', component: 'input', type: 'number', placeholder: 'Enter resting blood pressure', model: 'trtbps' },
        { id: 'chol', label: 'Total Cholesterol', component: 'input', type: 'number', placeholder: 'Enter total cholesterol', model: 'chol' },
        { id: 'fbs', label: 'Fasting Blood Sugar', component: 'input', type: 'number', placeholder: 'Enter fasting blood sugar', model: 'fbs' },
        { id: 'restecg', label: 'Resting Electrocardiogram', component: 'select', options: [{ value: 0, text: 'Normal' }, { value: 1, text: 'ST-T Wave Abnormality' }, { value: 2, text: 'Left Ventricular Hypertrophy' }], model: 'restecg' },
        { id: 'thalachh', label: 'Maximum Heart Rate Achieved', component: 'input', type: 'number', placeholder: 'Enter maximum heart rate', model: 'thalachh' },
        { id: 'exng', label: 'Exercise Induced Angina', component: 'select', options: [{ value: 0, text: 'No' }, { value: 1, text: 'Yes' }], model: 'exng' },
        { id: 'oldpeak', label: 'Oldpeak', component: 'input', type: 'number', placeholder: 'Enter oldpeak', model: 'oldpeak' },
        { id: 'slp', label: 'Slope of Peak Exercise ST Segment', component: 'select', options: [{ value: 0, text: 'Upsloping' }, { value: 1, text: 'Flat' }, { value: 2, text: 'Downsloping' }], model: 'slp' },
        { id: 'caa', label: 'Number of Major Blood Vessels', component: 'select', options: [{ value: 0, text: '0' }, { value: 1, text: '1' }, { value: 2, text: '2' }, { value: 3, text: '3' }], model: 'caa' },
        { id: 'thall', label: 'Thallium Stress Test', component: 'input', type: 'number', placeholder: 'Enter thallium stress test result', model: 'thall' }
      ]
    };
  },
  methods: {
    async getPrediction() {
      const features = this.formFields.reduce((acc, field) => {
        acc[field.model] = this[field.model];
        return acc;
      }, {});

      try {
        const response = await axios.post('http://localhost:5000/predict', features);
        this.prediction = response.data.prediction;
        console.log(this.prediction)
        this.deviations = response.data.deviations;
        console.log(this.deviations)
        this.showModal = true;
      } catch (error) {
        console.error("There was an error with the prediction:", error);
      }
    },
    closeModal() {
      this.showModal = false;
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px 0 0 100px;
  max-width: 90%;
}

input, select {
  width: 45%;
}

div.form-group {
  width: 80%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.modal-container {
  position: relative;
  margin: 10px;
}

.modal-content {
  background: white;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.modal-close {
  cursor: pointer;
}

.modal-close:hover {
  color: #f00;
}
</style> -->












<template>
    <div class="container mx-auto p-8 bg-gray-100 rounded-lg shadow-lg h-screen flex items-center">
      <h1 class="text-4xl font-bold text-center text-blue-700 mb-6">Patient Prediction Form</h1>


      <form @submit.prevent="getPrediction" class="prediction-form grid grid-cols-1 md:grid-cols-2 gap-4">

        <div class="form-group">
          <label for="gender" class="block text-sm font-medium text-gray-700">Gender</label>
          <select v-model.number="gender" id="gender" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Male</option>
            <option :value="1">Female</option>
          </select>
        </div>

        <div class="form-group">
          <label for="age" class="block text-sm font-medium text-gray-700" aria-valuemax="100" aria-valuemin="2">Age</label>
          <input v-model.number="age" type="number" placeholder="Enter age" id="age" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>

        <div class="form-group">
          <label for="hypertension" class="block text-sm font-medium text-gray-700">Hypertension</label>
          <select v-model.number="hypertension" id="hypertension" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Negative</option>
            <option :value="1">Positive</option>
          </select>
        </div>

        <div class="form-group">
          <label for="heart_disease" class="block text-sm font-medium text-gray-700">Heart Disease</label>
          <select v-model.number="heart_disease" id="heart_disease" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Negative</option>
            <option :value="1">Positive</option>
          </select>
        </div>

        <div class="form-group">
          <label for="ever_married" class="block text-sm font-medium text-gray-700">Ever Married</label>
          <select v-model.number="ever_married" id="ever_married" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">No</option>
            <option :value="1">Yes</option>
          </select>
        </div>

        

        <div class="form-group">
          <label for="work_type" class="block text-sm font-medium text-gray-700">Work Type</label>
          <select v-model.number="work_type" id="work_type" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">children</option>
            <option :value="1">Self-employed</option>
            <option :value="2">Govt_job</option>
            <option :value="3">Private</option>
            <option :value="4">Never_worked</option>
          </select>
        </div>

        <div class="form-group">
          <label for="Residence_type" class="block text-sm font-medium text-gray-700">Residence Type</label>
          <select v-model.number="residence_type" id="Residence_type" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Rural</option>
            <option :value="1">Urban</option>
          </select>
        </div>



        <div class="form-group">
          <label for="avg_glucose_level" class="block text-sm font-medium text-gray-700">Average Glucose Level</label>
          <input v-model.number="avg_glucose_level" type="number" placeholder="Enter resting blood pressure" id="avg_glucose_level" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="bmi" class="block text-sm font-medium text-gray-700">BMI</label>
          <input v-model.number="bmi" type="number" placeholder="Enter total cholesterol" id="bmi" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>


        <div class="form-group">
          <label for="smoking_status" class="block text-sm font-medium text-gray-700">Smoking Status</label>
          <select v-model.number="smoking_status" id="smoking_status" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Unknown</option>
            <option :value="1">never smoked</option>
            <option :value="2">formerly smoked</option>
            <option :value="3">smokes</option>
          </select>
        </div>

        <div class="col-span-1 md:col-span-2 flex justify-center">
          <button type="submit" class="submit-button w-full md:w-auto bg-blue-600 text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">Predict</button>
        </div>
      </form>
      <transition name="fade">
        <div v-if="prediction" class="prediction-result mt-6 p-4 bg-blue-100 border-l-4 border-blue-500 text-blue-700">
          Prediction: {{ prediction }}
        </div>
      </transition>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        gender:null,
        age:null, 
        hypertension:null, 
        heart_disease:null,
        ever_married:null,
        work_type:null, 
        residence_type:null,
        avg_glucose_level:null,
        bmi:null, smoking_status:null,
        prediction: null,
      };
    },
    methods: {
      async getPrediction() {
        const features = {
          gender: this.gender,
          age: this.age, 
          hypertension: this.hypertension, 
          heart_disease: this.heart_disease,
          ever_married: this.ever_married,
          work_type: this.work_type, 
          residence_type: this.residence_type,
          avg_glucose_level:this.avg_glucose_level,
          bmi:this.bmi,
          smoking_status:this.smoking_status,
      
        };
  
        try {
          const response = await axios.post('http://localhost:5001/predictStroke', features);
          console.log(features)
          this.prediction = response.data.prediction;
        } catch (error) {
          console.error("There was an error with the prediction:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    
    padding: 20px 0 0 100px;
    max-width: 90%;
    /* display: flex;
    flex-direction: column;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          */
 

  }

  input,select{
    width: 45%;
  }

  label{
    /* display: none; */
  }


  div.form-group{
    width: 80%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
  }
  </style>
