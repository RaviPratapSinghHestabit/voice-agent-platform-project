export default function Home() {
  return (
    <main
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
        fontFamily: "Arial"
      }}
    >
      <h1 style={{ fontSize: "3rem", marginBottom: "10px" }}>
        Voice Agent Platform
      </h1>

      <p style={{ marginBottom: "30px", color: "#555" }}>
        AI Powered Voice Assistant Platform
      </p>

      <div style={{ display: "flex", gap: "20px" }}>
        <a
          href="/login"
          style={{
            padding: "10px 20px",
            background: "black",
            color: "white",
            textDecoration: "none",
            borderRadius: "5px"
          }}
        >
          Login
        </a>

        <a
          href="/register"
          style={{
            padding: "10px 20px",
            border: "1px solid black",
            textDecoration: "none",
            borderRadius: "5px"
          }}
        >
          Register
        </a>
      </div>
    </main>
  );
}