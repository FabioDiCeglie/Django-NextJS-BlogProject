import PostPreview from "./post-preview";
import type Post from "../interfaces/post";

type Props = {
  articles: Post[];
};

const MoreStories = ({ articles }: Props) => {
  return (
    <section>
      <h2 className="mb-8 text-5xl md:text-7xl font-bold tracking-tighter leading-tight">
        More Stories
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-2 md:gap-x-16 lg:gap-x-32 gap-y-20 md:gap-y-32 mb-32">
        {articles.map((article) => (
          <PostPreview
            key={article.id}
            title={article.title}
            coverImage={article.coverImage}
            date={article.date}
            author_name={article.author_name}
            author_picture={article.author_picture}
            id={article.id}
            description={article.description}
          />
        ))}
      </div>
    </section>
  );
};

export default MoreStories;
