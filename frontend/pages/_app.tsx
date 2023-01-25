import { AppProps } from "next/app";
import "../styles/index.css";
import { CookiesProvider } from "react-cookie";

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <CookiesProvider>
      <Component {...pageProps} />
    </CookiesProvider>
  );
}
