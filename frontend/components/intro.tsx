import Link from "next/link";
import { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

const Intro = () => {
  const [token, setToken, removeToken] = useCookies(["mytoken"]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    if (token["mytoken"]) {
      setIsLoggedIn(true);
    }
  }, [isLoggedIn]);

  if (isLoggedIn) {
    return (
      <section className="flex-col md:flex-row flex items-center md:justify-between mt-16 mb-16 md:mb-12">
        <h1 className="text-5xl md:text-8xl font-bold tracking-tighter leading-tight md:pr-8">
          Blog.
        </h1>
        <button
          className="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
          onClick={() => {
            removeToken("mytoken");
            setIsLoggedIn(false);
          }}
        >
          Log out
        </button>
      </section>
    );
  } else {
    return (
      <section className="flex-col md:flex-row flex items-center md:justify-between mt-16 mb-16 md:mb-12">
        <h1 className="text-5xl md:text-8xl font-bold tracking-tighter leading-tight md:pr-8">
          Blog.
        </h1>
        <button className="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
          <Link href="/login">Log in</Link>
        </button>
      </section>
    );
  }
};

export default Intro;
