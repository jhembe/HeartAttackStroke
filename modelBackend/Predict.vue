<template>
    <div>
      <h1>Prediction</h1>
      
      <input v-model.number="age" placeholder="Age" />

      <label for="sex">Gender</label>
      <select v-model.number="sex">
      <option :value="0">Male</option>
      <option :value="1">Female</option>
    </select>

    <label for="chest_pain">Chest Pain Type</label>
    <select v-model.number="cp" id="chest_pain">
      <option :value="0">Typical Angina</option>
      <option :value="1">Atypical Angina</option>
      <option :value="1">Non-Anginal Pain</option>
      <option :value="1">Asymtomatic</option>
    </select>

    <label for="trtbps">Resting Blood Sugar</label>
      <input v-model.number="trtbps" placeholder="Resting Blood Sugar (trtbps)" />


      <input v-model.number="chol" placeholder="Total Cholesterol (chol)" />
      <input v-model.number="ldl" placeholder="LDL Cholesterol" />
      <input v-model.number="hdl" placeholder="HDL Cholesterol" />
      <input v-model.number="triglycerides" placeholder="Triglycerides" />
      <input v-model.number="fbs" placeholder="Fasting Blood Sugar (fbs)" />
      
      <label for="restecg">Resting Electrocardiogram (restecg)</label>
      <select v-model.number="restecg">
      <option :value="0">Normal</option>
      <option :value="1">ST-T Wave Abnormality with Inversions & depression</option>
      <option :value="1">Left ventricular Hypertrophy (Probable diagnosis or confirmed also)</option>
    </select>
      
      <input v-model.number="thalachh" placeholder="Maximum Heart Rate Achieved (thalachh)" />

      
      <input v-model.number="exeng" placeholder="Exercise Induced Angina (exeng)" />
      <label for="exeng">Exercise Induced Angina</label>
      <select v-model.number="sex">
      <option :value="0">No</option>
      <option :value="1">Yes</option>
    </select>


      <input v-model.number="oldpeak" placeholder="Oldpeak" />
      <input v-model.number="slope" placeholder="Slope of Peak Exercise ST Segment" />
      <input v-model.number="caa" placeholder="Number of Major Blood Vessels (caa)" />
      <input v-model.number="thall" placeholder="Thallium Stress Test (thall)" />
      <button @click="getPrediction">Predict</button>
      <div v-if="prediction">Prediction: {{ prediction }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        cp: null,
        trtbps: null,
        chol: null,
        ldl: null,
        hdl: null,
        triglycerides: null,
        fbs: null,
        restecg: null,
        thalachh: null,
        exeng: null,
        oldpeak: null,
        slope: null,
        caa: null,
        thall: null,
        prediction: null,
      };
    },
    methods: {
      async getPrediction() {
        const features = {
          cp: this.cp,
          trtbps: this.trtbps,
          chol: this.chol,
          ldl: this.ldl,
          hdl: this.hdl,
          triglycerides: this.triglycerides,
          fbs: this.fbs,
          restecg: this.restecg,
          thalachh: this.thalachh,
          exeng: this.exeng,
          oldpeak: this.oldpeak,
          slope: this.slope,
          caa: this.caa,
          thall: this.thall
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
  