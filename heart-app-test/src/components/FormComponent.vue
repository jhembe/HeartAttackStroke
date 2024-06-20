<template>
  <div class="container mx-auto p-8 bg-gray-100 rounded-lg shadow-lg h-screen flex items-center">
    <h1 class="text-4xl font-bold text-center text-blue-700 mb-6">Patient Prediction Form</h1>
    <form @submit.prevent="getPrediction" class="prediction-form grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Form Fields -->

      <div class="form-group">
          <label for="age" class="block text-sm font-medium text-gray-700" aria-valuemax="100" aria-valuemin="2">Age</label>
          <input v-model.number="age" type="number" placeholder="Enter age" id="age" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="sex" class="block text-sm font-medium text-gray-700">Gender</label>
          <select v-model.number="sex" id="sex" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Male</option>
            <option :value="1">Female</option>
          </select>
        </div>
        <div class="form-group">
          <label for="cp" class="block text-sm font-medium text-gray-700">Chest Pain Type</label>
          <select v-model.number="cp" id="cp" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Typical Angina</option>
            <option :value="1">Atypical Angina</option>
            <option :value="2">Non-Anginal Pain</option>
            <option :value="3">Asymptomatic</option>
          </select>
        </div>
        <div class="form-group">
          <label for="trtbps" class="block text-sm font-medium text-gray-700">Resting Blood Pressure</label>
          <input v-model.number="trtbps" type="number" placeholder="Enter resting blood pressure" id="trtbps" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="chol" class="block text-sm font-medium text-gray-700">Total Cholesterol</label>
          <input v-model.number="chol" type="number" placeholder="Enter total cholesterol" id="chol" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="fbs" class="block text-sm font-medium text-gray-700">Fasting Blood Sugar</label>
          <input v-model.number="fbs" type="number" placeholder="Enter fasting blood sugar" id="fbs" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="restecg" class="block text-sm font-medium text-gray-700">Resting Electrocardiogram</label>
          <select v-model.number="restecg" id="restecg" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Normal</option>
            <option :value="1">ST-T Wave Abnormality</option>
            <option :value="2">Left Ventricular Hypertrophy</option>
          </select>
        </div>
        <div class="form-group">
          <label for="thalachh" class="block text-sm font-medium text-gray-700">Maximum Heart Rate Achieved</label>
          <input v-model.number="thalachh" type="number" placeholder="Enter maximum heart rate" id="thalachh" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="exng" class="block text-sm font-medium text-gray-700">Exercise Induced Angina</label>
          <select v-model.number="exng" id="exng" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">No</option>
            <option :value="1">Yes</option>
          </select>
        </div>
        <div class="form-group">
          <label for="oldpeak" class="block text-sm font-medium text-gray-700">Oldpeak</label>
          <input v-model.number="oldpeak" type="number" placeholder="Enter oldpeak" id="oldpeak" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="slp" class="block text-sm font-medium text-gray-700">Slope of Peak Exercise ST Segment</label>
          <select v-model.number="slp" id="slp" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Upsloping</option>
            <option :value="1">Flat</option>
            <option :value="2">Downsloping</option>
          </select>
        </div>
        <div class="form-group">
          <label for="caa" class="block text-sm font-medium text-gray-700">Number of Major Blood Vessels</label>
          <select v-model.number="caa" id="caa" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">0</option>
            <option :value="1">1</option>
            <option :value="2">2</option>
            <option :value="3">3</option>
          </select>
        </div>
        <div class="form-group">
          <label for="thall" class="block text-sm font-medium text-gray-700">Thallium Stress Test</label>
          <input v-model.number="thall" type="number" placeholder="Enter thallium stress test result" id="thall" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>


      <div class="col-span-1 md:col-span-2 flex justify-center">
        <button type="submit" class="submit-button w-full md:w-auto bg-blue-600 text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">Predict</button>
      </div>
    </form>

    <!-- Modal -->
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
              <p><strong>Prediction:</strong> {{ fate }}</p>
              <div v-if="deviations && Object.keys(deviations).length > 0">
                <p><strong>Probable Causes:</strong></p>
                <ul>
                  <li v-for="(value, feature) in deviations" :key="feature">
                    {{ feature }}: {{ value }}
                  </li>
                </ul>
                <p><strong>Recomendation : </strong>{{ recomendation }}</p>
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
        recomendation:'',
        fate:''
    };
  },
  methods: {
    async getPrediction() {
      try {
        const features = {
          age: this.age,
          sex: this.sex,
          cp: this.cp,
          trtbps: this.trtbps,
          chol: this.chol,
          fbs: this.fbs,
          restecg: this.restecg,
          thalachh: this.thalachh,
          exng: this.exng,
          oldpeak: this.oldpeak,
          slp: this.slp,
          caa: this.caa,
          thall: this.thall
        };
        
        console.log("Form Data: ", features); // Log the data to verify
        
        const response = await axios.post('http://localhost:5000/predict', features);
        
        console.log("API Response: ", response.data); // Log the response to verify
        console.log("Deviation Two",response.data.deviations);
        console.log("Prediction One:",response.data.prediction)

        if(response.data.prediction[0] === 1){
          this.fate = "You have a high risk of getting a Heart Attack"
          this.recomendation = "Proper Diagnosis"
        }
        this.prediction = response.data.prediction;
        this.deviations = response.data.deviations;
        console.log("Prediction Two: ",this.prediction)
        console.log("Deviation Two : ",this.deviations)
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
</style>







<!-- 
<template>
    <div class="container mx-auto p-8 bg-gray-100 rounded-lg shadow-lg h-screen flex items-center">
      <h1 class="text-4xl font-bold text-center text-blue-700 mb-6">Patient Prediction Form</h1>
      <form @submit.prevent="getPrediction" class="prediction-form grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="form-group">
          <label for="age" class="block text-sm font-medium text-gray-700" aria-valuemax="100" aria-valuemin="2">Age</label>
          <input v-model.number="age" type="number" placeholder="Enter age" id="age" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="sex" class="block text-sm font-medium text-gray-700">Gender</label>
          <select v-model.number="sex" id="sex" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Male</option>
            <option :value="1">Female</option>
          </select>
        </div>
        <div class="form-group">
          <label for="cp" class="block text-sm font-medium text-gray-700">Chest Pain Type</label>
          <select v-model.number="cp" id="cp" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Typical Angina</option>
            <option :value="1">Atypical Angina</option>
            <option :value="2">Non-Anginal Pain</option>
            <option :value="3">Asymptomatic</option>
          </select>
        </div>
        <div class="form-group">
          <label for="trtbps" class="block text-sm font-medium text-gray-700">Resting Blood Pressure</label>
          <input v-model.number="trtbps" type="number" placeholder="Enter resting blood pressure" id="trtbps" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="chol" class="block text-sm font-medium text-gray-700">Total Cholesterol</label>
          <input v-model.number="chol" type="number" placeholder="Enter total cholesterol" id="chol" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="fbs" class="block text-sm font-medium text-gray-700">Fasting Blood Sugar</label>
          <input v-model.number="fbs" type="number" placeholder="Enter fasting blood sugar" id="fbs" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="restecg" class="block text-sm font-medium text-gray-700">Resting Electrocardiogram</label>
          <select v-model.number="restecg" id="restecg" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Normal</option>
            <option :value="1">ST-T Wave Abnormality</option>
            <option :value="2">Left Ventricular Hypertrophy</option>
          </select>
        </div>
        <div class="form-group">
          <label for="thalachh" class="block text-sm font-medium text-gray-700">Maximum Heart Rate Achieved</label>
          <input v-model.number="thalachh" type="number" placeholder="Enter maximum heart rate" id="thalachh" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="exng" class="block text-sm font-medium text-gray-700">Exercise Induced Angina</label>
          <select v-model.number="exng" id="exng" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">No</option>
            <option :value="1">Yes</option>
          </select>
        </div>
        <div class="form-group">
          <label for="oldpeak" class="block text-sm font-medium text-gray-700">Oldpeak</label>
          <input v-model.number="oldpeak" type="number" placeholder="Enter oldpeak" id="oldpeak" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
        </div>
        <div class="form-group">
          <label for="slp" class="block text-sm font-medium text-gray-700">Slope of Peak Exercise ST Segment</label>
          <select v-model.number="slp" id="slp" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">Upsloping</option>
            <option :value="1">Flat</option>
            <option :value="2">Downsloping</option>
          </select>
        </div>
        <div class="form-group">
          <label for="caa" class="block text-sm font-medium text-gray-700">Number of Major Blood Vessels</label>
          <select v-model.number="caa" id="caa" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
            <option :value="0">0</option>
            <option :value="1">1</option>
            <option :value="2">2</option>
            <option :value="3">3</option>
          </select>
        </div>
        <div class="form-group">
          <label for="thall" class="block text-sm font-medium text-gray-700">Thallium Stress Test</label>
          <input v-model.number="thall" type="number" placeholder="Enter thallium stress test result" id="thall" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"/>
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
      };
    },
    methods: {
      async getPrediction() {
        const features = {
          age: this.age,
          sex: this.sex,
          cp: this.cp,
          trtbps: this.trtbps,
          chol: this.chol,
          fbs: this.fbs,
          restecg: this.restecg,
          thalachh: this.thalachh,
          exng: this.exng,
          oldpeak: this.oldpeak,
          slp: this.slp,
          caa: this.caa,
          thall: this.thall,
        };
  
        try {
          const response = await axios.post('http://localhost:5000/predict', features);
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
  </style> -->
