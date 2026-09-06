<template>
  <div class="admin-container">
    <div class="sidebar">
      <div>
        <div class="text-5xl font-extrabold tracking-tighter text-primary mb-6 p-2">
          <span>Fixin</span><span class="text-white drop-shadow-md">IT</span>
          <p class="text-xl font-bold">Ruang Kendali</p>
        </div>
      </div>
      <ul>
        <li><router-link to="/Admin_users" class="block w-full">Data Pengguna</router-link></li>
        <li><router-link to="/Admin" class="block w-full">Data Pengaduan</router-link></li>
      </ul>
    </div>

    <div class="content">
      <h1 class="text-4xl font-bold text-gray-800 mb-8 mt-4">Data Pengguna</h1>

      <div v-if="loading" class="py-8">Memuat data pengguna...</div>

      <div v-else>
        <div v-if="unauthorized" class="p-6 bg-yellow-50 border-l-4 border-yellow-400 text-yellow-700">
          <p>{{ unauthMessage }}</p>
          <div class="mt-4">
            <button
              v-if="unauthMessage.includes('login')"
              @click="router.push('/login')"
              class="px-3 py-2 bg-yellow-400 rounded font-bold"
            >
              Ke Halaman Masuk
            </button>
          </div>
        </div>

        <div v-else>
          <router-link to="/Admin" class="px-4 py-2 bg-amber-400 text-white rounded hover:bg-amber-500 mt-4 inline-block">
            Kembali ke Laporan
          </router-link>

          <table class="data-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nama</th>
                <th>Email</th>
                <th>Role</th>
                <th>Tanggal Dibuat</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.namaLengkap }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <span :class="user.role === 'admin' ? 'text-amber-500 font-bold' : 'text-sky-500 font-bold'">
                    {{ user.role }}
                  </span>
                </td>
                <td>{{ formatDate(user.dibuatPada) }}</td>
              </tr>
              <tr v-if="users.length === 0">
                <td colspan="5" class="text-center py-4 text-gray-500">Belum ada pengguna terdaftar.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "./api.js";

const router = useRouter();
const users = ref([]);
const loading = ref(true);
const unauthorized = ref(false);
const unauthMessage = ref("");

const formatDate = (value) => {
  if (!value) return "-";

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;

  return date.toLocaleString("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const getAuthHeaders = () => {
  const token = localStorage.getItem("token");
  return {
    Authorization: token ? `Bearer ${token}` : "",
  };
};

const ambilData = async () => {
  loading.value = true;
  try {
    const res = await api.get("/api/admin/users", {
      headers: getAuthHeaders(),
    });
    users.value = res.data.users || [];
    unauthorized.value = false;
    unauthMessage.value = "";
  } catch (error) {
    const status = error.response?.status;

    if (status === 401) {
      unauthorized.value = true;
      unauthMessage.value = "Anda belum masuk. Silakan login untuk mengakses dashboard admin.";
    } else if (status === 403) {
      unauthorized.value = true;
      unauthMessage.value = "Anda tidak memiliki wewenang untuk mengakses dashboard ini.";
    } else {
      unauthorized.value = true;
      unauthMessage.value = "Gagal memuat data pengguna. Silakan coba lagi nanti.";
    }
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  ambilData();
});
</script>

<style scoped>
.admin-container {
  display: flex;
  min-height: 100vh;
  font-family: Arial, sans-serif;
}

.sidebar {
  width: 250px;
  background-color: #fbbf24;
  color: white;
  padding: 20px;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
  margin-top: 20px;
}

.sidebar li {
  padding: 12px 0;
  border-bottom: 1px solid #ffffff;
  cursor: pointer;
}

.sidebar li:hover {
  color: #f5db71;
}

.content {
  flex: 1;
  padding: 30px;
  background-color: #f8f9fa;
}

.data-table {
  width: 100%;
  background-color: white;
  margin-top: 20px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 12px;
  overflow: hidden;
}

.data-table th,
.data-table td {
  padding: 15px;
  border: 1px solid #e0e0e0;
  text-align: left;
}

.data-table th {
  background-color: #fbbf24;
  color: #ffffff;
  font-weight: bold;
  text-align: center;
}

.data-table tr:hover {
  background-color: #f9f9f9;
}
</style>
